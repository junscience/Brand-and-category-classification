# Embeddings
Define name of brand and category with local base and embeddings tools. The program uses uvicorn engine to take the name of a product and to give it name of a brand and category. These parameters will be build in lancedb table "Embeddings_db". 

Use `docker build -t "Embeddings_project" .` to make a container

Use `docker run -e LANCEDB_CONFIG_DIR=/tmp -p 8000:8000 Embeddings_project` to start an uvicorn server. 
