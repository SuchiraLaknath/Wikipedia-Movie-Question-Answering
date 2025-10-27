from .read__write_json import read_json_file, write_json_file
from .read_yml import read_yml_file
from .write_svg import write_svg
from .read_txt import read_txt_file
import os

def read_file(file_path, directory = None):
    if directory:
        file_path = os.path.join(directory, file_path)
    if file_path.endswith(".json"):
        return read_json_file(file_path= file_path)
    
    elif file_path.endswith(".yml"):
        return read_yml_file(file_path= file_path)
    
    elif file_path.endswith(".yaml"):
        return read_yml_file(file_path= file_path)
    
    elif file_path.endswith(".txt"):
        return read_txt_file(file_path= file_path)

    else:
        raise Exception(f"Currently only support to json, yml, txt, and yaml")


def write_file(data, file_path, directory = None):
    if directory:
        file_path = os.path.join(directory, file_path)

    if file_path.endswith(".json"):
        write_json_file(dictionary= data, file_path= file_path)

    elif file_path.endswith(".svg"):
        write_svg(data= data, file_path= file_path)

    else:
        raise Exception(f"Currently only support to json , svg files")
    