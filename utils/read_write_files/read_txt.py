
def read_txt_file(file_path, strip_end = True):
    try:
        with open(file_path, "r") as f:
            contents = f.read()
        return contents
    except Exception as e:
        raise Exception(f"Error loading txt file: {str(e)}")