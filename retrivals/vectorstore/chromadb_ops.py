from chromadb.utils import embedding_functions
import chromadb
import configs
import pandas as pd
from utils.json_processings import get_nested
import os

os.environ["ANONYMIZED_TELEMETRY"] = "false"

def read_csv_file(file_path, deliminator = ','):
    return pd.read_csv(file_path, delimiter= deliminator)

class ChromaDB:

    def __init__(self):
        embedding_api_key = os.getenv('OPENAI_API_KEY')
        client = chromadb.PersistentClient(path=configs.CHROMA_DB_DIR)
        embedding_fn = self.get_embedding_fn(embedding_api_key = embedding_api_key)
        self.collection = client.get_or_create_collection(
            name=configs.COLLECTION_NAME,
            embedding_function=embedding_fn)


    def get_embedding_fn(self, embedding_api_key):
        return embedding_functions.OpenAIEmbeddingFunction(
                    api_key=embedding_api_key,
                    model_name= configs.embedding_model
                )
    
    def upsert_data_chunk(self, data_chunk, id):
        self.collection.upsert(
                    documents=[
                        str(data_chunk)
                    ],
                    ids=[f"{id}"]
                )
        
    def retrive_documenets(self, query_text, number_of_chunks = 5):
        results = self.collection.query(
            query_texts=[query_text], # Chroma will embed this for you
            n_results=number_of_chunks # how many results to return
            )
        
        return get_nested(dictionary= results, key= 'documents')
