import pandas as pd
from utils.json_processings import get_nested
import configs
from retrivals.vectorstore.chromadb_ops import ChromaDB
from dotenv import load_dotenv
import os
from tqdm import tqdm

_ = load_dotenv()

chromadb_obj = ChromaDB()

def limit_words(text: str, max_words: int, suffix: str = "…") -> str:
    words = text.split()
    return " ".join(words[:max_words]) + (suffix if len(words) > max_words else "")

def read_csv_file(file_path, deliminator = ','):
    return pd.read_csv(file_path, delimiter= deliminator)

def read_csv_and_injest_to_chrmadb(file_path, maximum_rows, deliminator = ','):
    df = read_csv_file(file_path= file_path, deliminator= deliminator)
    if len(df)> maximum_rows:
        df = df[:maximum_rows]
    for index, row in tqdm(df.iterrows()):
        title = get_nested(dictionary= row, key= "Title")
        plot = get_nested(dictionary= row, key= "Plot")
        chunked_plot = limit_words(text=plot, max_words= configs.CHUNK_SIZE)
        
        if title != None:
            try:
                data_chunk = f"{title} :- {chunked_plot}"
                chromadb_obj.upsert_data_chunk(data_chunk= data_chunk, id= index)
            except:
                print(f"Failed storing movie {title}")

    print(f"Data storing process has been finished")
    