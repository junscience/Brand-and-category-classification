# Embeddings
Define name of brand and category with local base and embeddings tools. The program uses uvicorn engine to take the name of a product and to give it name of a brand and category. These parameters will be build in lancedb table "Embeddings_db". 

Use ```git clone https://github.com/junscience/Embeddings``` to copy project to your directory. 


Use ```docker build -t "Embeddings_project" .``` to make a container

Use ```docker run -e LANCEDB_CONFIG_DIR=/tmp -p 8000:8000 Embeddings_project``` to start an uvicorn server. 

You can explore lancedb file with commands in python:

```
import lancedb
import pandas as pd

uri = "data/sample-lancedb"
db = lancedb.connect(uri)
tbl = db.open_table("Embeddings_db")
DB = tbl.to_pandas()
```
