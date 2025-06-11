# Graphiti Quickstart

Graphiti is a powerful framework designed to help you build and manage dynamic knowledge graphs. It provides tools and functionalities to interact with graph databases like Neo4j, enabling you to store, query, and analyze complex relationships within your data.

## Project Overview

This quickstart project demonstrates how to use Graphiti to:

- **Load knowledge into a Neo4j graph database:** The `llm_knowledge.py` script populates the graph with information about the evolution of Large Language Models (LLMs).
- **Perform various types of searches:** The `connection.py` file defines different search methods to query the graph.
- **Integrate with a Python application:** The `quickstart.py` file orchestrates the data loading and interaction with the Graphiti framework.

## Knowledge Loading via Neo4j and `quickstart.py`

Knowledge is loaded into the Neo4j database through the `llm_knowledge.py` script, which is invoked by `quickstart.py`. The `llm_knowledge.py` script defines a series of "phases" that represent different stages in the evolution of LLMs. Each phase adds `Episode` nodes and establishes relationships between them, effectively building a timeline of LLM development.

Before loading new data, the `check_llm_data_exists` function in `llm_knowledge.py` verifies if LLM knowledge data already exists in the graph. This prevents redundant data loading if the graph has already been populated.

The `quickstart.py` file serves as the main entry point for the application. It initializes the Graphiti connection, calls `run_llm_knowledge_demo` from `llm_knowledge.py` to load the data, and then proceeds with other functionalities, such as performing searches.

## Types of Searches in `connection.py`

The `connection.py` file provides methods for interacting with the Neo4j database and performing different types of searches. Here are some key search methods:

- **`hybrid_search`**: This method likely combines different search techniques (e.g., keyword search, graph traversal) to provide comprehensive results. It's designed to leverage the interconnected nature of graph data to find relevant information.

- **`center_node_search`**: This method focuses on finding information related to a central node in the graph. It's useful for exploring the neighborhood of a specific entity and understanding its direct and indirect relationships.

-   **`node search using reciepe`**: Graphiti provides predefined search recipes optimized for different search scenarios. Here we use NODE_HYBRID_SEARCH_RRF for retrieving nodes directly instead of edges.

These search functions allow you to effectively retrieve and analyze the knowledge stored in your Graphiti knowledge graph.

## Prerequisites

Before you begin, ensure you have the following installed and set up:

-   **Neo4j:** The project uses Neo4j as its graph database. You can run it via Docker as described in the "Getting Started" section.
-   **Python 3.9+:** The application is built with Python.
-   **OpenAI API Key:** An OpenAI API key is required for certain functionalities (e.g., LLM interactions).

## Environment Variables (`.env` file)

Create a `.env` file in the root directory of the project with the following attributes:

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_neo4j_password
OPENAI_API_KEY=your_openai_api_key
MODEL_CHOICE=gpt-4.1-mini # or other OpenAI model
```

Replace `your_neo4j_password` and `your_openai_api_key` with your actual credentials.

## Getting Started

To get this project up and running, follow these steps:

1.  **Neo4j Setup:**
    The simplest way to install Neo4j is via Neo4j Desktop. It provides a user-friendly interface to manage Neo4j instances and databases. Api port is localhost:7687 and browser port is localhost 7474


2.  **Run**
    ```bash
    python quickstart.py
    ```
3. ** Live Agent (Optional)**

   this is an interative agent which will connect to your knowledge graph and augments the answers from LLM.
   ```bash
    python live_agent.py
     ```
