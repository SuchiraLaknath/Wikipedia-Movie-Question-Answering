import pandas as pd
import configs
from langchain_community.document_loaders.csv_loader import CSVLoader
from chromadb.utils import embedding_functions
import chromadb
from dotenv import load_dotenv
import pandas as pd
import os

from dotenv import load_dotenv
from retrivals.store_csv_to_vdb import read_csv_and_injest_to_chrmadb
import configs
_ = load_dotenv()


def add_data_to_vdb():
    read_csv_and_injest_to_chrmadb(file_path= configs.CSV_PATH, maximum_rows= configs.SUBSET_SIZE)


if __name__ == "__main__":
    add_data_to_vdb()