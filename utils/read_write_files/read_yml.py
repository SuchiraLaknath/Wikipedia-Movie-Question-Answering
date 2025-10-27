import yaml

def read_yml_file(file_path):
    try:
        with open(file_path, "r") as f:
            contents = yaml.safe_load(f)
            return contents
    except Exception as e:
        raise Exception(f"Error loading YML file: {str(e)}")