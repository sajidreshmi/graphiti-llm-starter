import json
import os
from datetime import datetime, timezone
from typing import Dict, List, Union

from graphiti_core import Graphiti
from graphiti_core.edges import EntityEdge
from graphiti_core.nodes import EpisodeType
from graphiti_core.search.search_config import SearchConfig
from graphiti_core.utils.maintenance import clear_data
from graphiti_core.search.search_config_recipes import NODE_HYBRID_SEARCH_RRF


class Connection:
    def __init__(self):
        neo4j_uri = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
        neo4j_user = os.environ.get("NEO4J_USER", "neo4j")
        neo4j_password = os.environ.get("NEO4J_PASSWORD", "password")

        if not neo4j_uri or not neo4j_user or not neo4j_password:
            raise ValueError(
                "NEO4J_URI, NEO4J_USER, and NEO4J_PASSWORD must be set")

        self.graphiti = Graphiti(neo4j_uri, neo4j_user, neo4j_password)

    async def add_episodes(graphiti, episodes, prefix="LLM Evolution"):
        """Add episodes to the graph with a given prefix."""
        for i, episode in enumerate(episodes):
            await graphiti.add_episode(
                name=f'{prefix} {i}',
                episode_body=episode['content']
                if isinstance(episode['content'], str)
                else json.dumps(episode['content']),
                source=episode['type'],
                source_description=episode['description'],
                reference_time=datetime.now(timezone.utc),
            )
            print(f'Added episode: {prefix} {i} ({episode["type"].value})')

    async def hybrid_search(self, query: str):
        try:
            results = await self.graphiti.search(query)
            # Print search results
            print('\nSearch Results:')
            for result in results:
                print(f'UUID: {result.uuid}')
                print(f'Fact: {result.fact}')
                if hasattr(result, 'valid_at') and result.valid_at:
                    print(f'Valid from: {result.valid_at}')
                if hasattr(result, 'invalid_at') and result.invalid_at:
                    print(f'Valid until: {result.invalid_at}')
                print('---')
                return results
        finally:
            print("\nSearch Complete !!")

    async def center_node_search(self, query: str, results: list[EntityEdge]):

        # Use the top search result's UUID as the center node for reranking
        try:
            if results and len(results) > 0:
                center_node_uuid = results[0].source_node_uuid

                print('\nReranking search results based on graph distance:')
                print(f'Using center node UUID: {center_node_uuid}')

                reranked_results = await self.graphiti.search(
                    query, center_node_uuid=center_node_uuid
                )

                # Print reranked search results
                print('\nReranked Search Results:')
                for result in reranked_results:
                    print(f'UUID: {result.uuid}')
                    print(f'Fact: {result.fact}')
                    if hasattr(result, 'valid_at') and result.valid_at:
                        print(f'Valid from: {result.valid_at}')
                    if hasattr(result, 'invalid_at') and result.invalid_at:
                        print(f'Valid until: {result.invalid_at}')
                print('---')
            else:
                print("No results found in the initial search to use as center node.")
        finally:
            print(
                "\nCenter Node Search: results found in the initial search to use as center node."
            )

    async def node_search_by_recipe(self, query: str):
        # Example: Perform a node search using _search method with standard recipes
        print(
            '\nPerforming node search using _search method with standard recipe NODE_HYBRID_SEARCH_RRF:'
        )
        try:
            # Use a predefined search configuration recipe and modify its limit
            node_search_config = NODE_HYBRID_SEARCH_RRF.model_copy(deep=True)
            node_search_config.limit = 5  # Limit to 5 results

            node_search_results = await self.graphiti._search(
                query=query,
                config=node_search_config,
            )
            # Print node search results
            print("\nNode Search Results:")
            for node in node_search_results.nodes:
                print(f"Node UUID: {node.uuid}")
                print(f"Node Name: {node.name}")
                node_summary = (
                    node.summary[:100] + "..."
                    if len(node.summary) > 100
                    else node.summary
                )
                print(f"Content Summary: {node_summary}")
                print(f'Node Labels: {", ".join(node.labels)}')
                print(f"Created At: {node.created_at}")
                if hasattr(node, "attributes") and node.attributes:
                    print("Attributes:")
                    for key, value in node.attributes.items():
                        print(f"  {key}: {value}")
                print("---")
        finally:
            print("\nNode Search By Recipe Complete !!")

    async def close(self):
        await self.graphiti.close()
        print("connection closed !!")

    async def clear_data(self):
        await clear_data(self.graphiti.driver)
        print("Clearing Previous Data")
