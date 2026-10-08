# Graph-Based Recipe Recommendation Engine with RAG and Neo4j

Introduction to Data Science, Assignment 3.

This project answers recipe questions in two ways. It stores recipes as a graph in Neo4j and lets an LLM write Cypher queries to search it. It also runs a hybrid RAG pipeline that mixes keyword search (BM25) with vector search (FAISS). The answers are scored with RAGAS.

## What it does

1. **Load and split.** Loads recipes from TXT, Markdown, HTML and a Python file. Compares recursive, token and semantic splitting.
2. **Embed and store.** Makes embeddings with `all-MiniLM-L6-v2` and stores them in FAISS. Builds a BM25 retriever on the same chunks.
3. **Graph database.** Stores recipes in Neo4j with `Recipe`, `Ingredient` and `Cuisine` nodes, linked by `CONTAINS` and `BELONGS_TO`.
4. **Graph QA.** Uses `GraphCypherQAChain` with Llama 3.3 70B on Groq to turn questions into Cypher queries.
5. **Hybrid RAG.** Combines BM25 and vector results, then asks the LLM to answer from that context only.
6. **Evaluation.** Scores 5 question and answer pairs with RAGAS.

## Results

| Metric | Score |
| --- | --- |
| Faithfulness | 0.875 |
| Answer relevancy | 0.786 |
| Context precision | 0.483 |

Sample graph query:

```
Question: What recipes contain chocolate?
Cypher:   MATCH (r:Recipe)-[:CONTAINS]->(i:Ingredient {name: 'chocolate'}) RETURN r.name
Answer:   Chocolate Lava Cake contains chocolate.
```

## Project structure

```
notebook/  Jupyter notebook (made in Google Colab)
data/      Recipe files in TXT, MD, HTML and Python
report/    Assignment report (PDF)
```

## How to run

1. Install the packages:
   ```
   pip install -r requirements.txt
   ```
2. Create a free Neo4j Aura database at https://neo4j.com/cloud/aura and get a Groq API key at https://console.groq.com.
3. Open `notebook/recipe_graph_rag.ipynb` and put in your Neo4j URL, password and Groq key.
4. Put the files from `data/` next to the notebook and run all cells.

## Tools

Python, LangChain, Neo4j, Groq (Llama 3.3 70B), FAISS, BM25, Hugging Face sentence transformers, RAGAS.
