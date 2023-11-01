from utils.es_service import ElasticSearchClassService
import pandas as pd
import os
from dotenv import load_dotenv
import sys

load_dotenv()
ES_HOST = str(os.getenv("ES_HOST", "127.0.0.1"))
ES_USERNAME = str(os.getenv("ELASTIC_USERNAME", "elastic"))
ES_PASSWORD = str(os.getenv("ELASTIC_PASSWORD", "rootpass"))

sys.tracebacklimit = 0
DEFAULT_LIMIT = 1000
DIM_TEXT_FEATURE = 768
MAPPING_DICT = {
  "properties": {
    "id": {
      "type": "text"
    },
    "title": {
      "type": "text"
    },
    "title_vector": {
      "type": "dense_vector",
      "dims": DIM_TEXT_FEATURE
    }
  }
}

def load_csv():
  current_dir = os.path.dirname(os.path.realpath(__file__))
  data_folder = os.path.join(current_dir, "data", "title.csv")
  df = pd.read_csv(data_folder).fillna(" ")
  return df

if __name__ == "__main__":
  try:
    
    host = f"http://{ES_USERNAME}:{ES_PASSWORD}@{ES_HOST}:9200"
    print(f"Establishing connection to {host}")
    es_service = ElasticSearchClassService(hosts=host)
    print("1. Create index")

    es_service.create_index(mapping=MAPPING_DICT)
    print("2. Start indexing")

    df = load_csv()
    count = 0
    docs = []
    
    limit = int(input(f"Enter the number of rows to index (minimum {DEFAULT_LIMIT}): "))
    if  limit < DEFAULT_LIMIT:
      limit = DEFAULT_LIMIT
    for _, row in df.iterrows():
      count += 1
      item = { "id": row["id"], "title": row["title"] }
      docs.append(item)
      if count % DEFAULT_LIMIT == 0:
        es_service.bulk_index_data(docs=docs)
        es_service.refresh_index()
        docs = []
        print("Indexed {} documents.".format(count))
        if count >= limit:
          break
    print("3. Finished indexing")
  except KeyboardInterrupt:
    print("Indexing interrupted")
