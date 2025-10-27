import json

def read_json_file(file_path, ecnoding = 'utf-8'):
    try:
        with open(file_path, 'r', encoding=ecnoding) as file:
            data = json.load(file)
        return data
    except Exception as e:
        raise Exception(f"Error loading JSON file: {str(e)}")
    

def write_json_file(dictionary, file_path, indent:int=4, ecnoding = 'utf-8'):
    try:
        with open(file_path, "w", encoding= ecnoding) as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=indent)
    except Exception as e:
        raise Exception(f"Error writing JSON file: {str(e)}")