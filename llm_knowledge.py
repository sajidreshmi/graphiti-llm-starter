"""
LLM Knowledge Script

This script demonstrates the evolution of LLMs over time using Graphiti.
It creates episodes about different LLMs, then updates them to show how
the field evolves over time.
"""

import asyncio
import json
import logging
import os
from datetime import datetime, timezone
from logging import INFO

from dotenv import load_dotenv
from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType
from graphiti_core.utils.maintenance.graph_data_operations import clear_data
from connection import Connection
from llm_constants import *


class LLM_Knowledge:
    """LLM Knowledge Class"""

    def __init__(self):
        logging.basicConfig(
            level=INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )
        # Configure logging
        logger = logging.getLogger(__name__)

        load_dotenv()

        # Neo4j connection parameters
        neo4j_uri = os.environ.get('NEO4J_URI', 'bolt://localhost:7687')
        neo4j_user = os.environ.get('NEO4J_USER', 'neo4j')
        neo4j_password = os.environ.get('NEO4J_PASSWORD', 'password')

        if not neo4j_uri or not neo4j_user or not neo4j_password:
            raise ValueError(
                'NEO4J_URI, NEO4J_USER, and NEO4J_PASSWORD must be set')

    async def check_llm_data_exists(self, graphiti):
        """Check if LLM knowledge data already exists in the graph."""
        result = await graphiti.driver.execute_query("MATCH (n1)-[r]->(n2) RETURN * LIMIT 1")
        return bool(result.records)

    async def get_user_choice(self):
        """Get user choice to continue or quit."""
        while True:
            choice = input(
                "\nType 'continue' to proceed or 'quit' to exit: ").strip().lower()
            if choice in ['continue', 'quit']:
                return choice
            print("Invalid input. Please type 'continue' or 'quit'.")

    async def phase1_current_llms(self, graphiti):
        """Phase 1: Add episodes about current top LLMs."""
        print("\n=== PHASE 1: CURRENT TOP LLMs ===")

        # Episodes about current LLMs
        episodes = PHASE1_EPISODES

        await Connection.add_episodes(graphiti, episodes, "Current LLMs")

        # Perform a search to show the results
        print("\nSearching for: 'Which is the best LLM?'")
        results = await graphiti.search('Which is the best LLM?')

        print('\nSearch Results:')
        for result in results:
            print(f'Fact: {result.fact}')
            print('---')

    async def phase2_claude4_emerges(self, graphiti):
        """Phase 2: Claude 4 emerges as the new best LLM."""
        print("\n=== PHASE 2: CLAUDE 4 EMERGES ===")

        # Episodes about Claude 4 becoming the best LLM
        episodes = PHASE2_EPISODES

        await Connection.add_episodes(graphiti, episodes, "Claude 4 Era")

        # Perform a search to show the results
        print("\nSearching for: 'Which is the best LLM now?'")
        results = await graphiti.search('Which is the best LLM now?')

        print('\nSearch Results:')
        for result in results:
            print(f'Fact: {result.fact}')
            print('---')

    async def phase3_mlm_revolution(self, graphiti):
        """Phase 3: MLMs make LLMs irrelevant."""
        print("\n=== PHASE 3: MLM REVOLUTION ===")

        # Episodes about MLMs replacing LLMs
        episodes = PHASE3_EPISODES

        await Connection.add_episodes(graphiti, episodes, "MLM Revolution")

        # Perform a search to show the results
        print("\nSearching for: 'Are LLMs still relevant?'")
        results = await graphiti.search('Are LLMs still relevant?')

        print('\nSearch Results:')
        for result in results:
            print(f'Fact: {result.fact}')
            print('---')

    async def run_llm_knowledge_demo(self, graphiti):
        """Main function to run the LLM evolution demonstration."""
        try:
            if await self.check_llm_data_exists(graphiti):
                print("LLM knowledge data already exists. Skipping data loading.")
            else:
                # Clear existing data
                print("Do you want to clear existing data?")
                choice = await self.get_user_choice()
                if choice == 'quit':
                    return

                print("Clearing existing graph data...")
                await clear_data(graphiti.driver)
                print("Graph data cleared successfully.")

                # Phase 1: Current top LLMs with Gemini 2.5 Pro as the best
                await self.phase1_current_llms(graphiti)

                # Wait for user input
                choice = await self.get_user_choice()
                if choice == 'quit':
                    return

                # Phase 2: Claude 4 emerges as the new best LLM
                await self.phase2_claude4_emerges(graphiti)

                # Wait for user input
                choice = await self.get_user_choice()
                if choice == 'quit':
                    return

                # Phase 3: MLMs make LLMs irrelevant
                await self.phase3_mlm_revolution(graphiti)

        finally:
            # Close the connection
            await graphiti.close()
            print('\nConnection closed')
