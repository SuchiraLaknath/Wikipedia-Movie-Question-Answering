
def write_svg(data, file_path):
    try:
        with open(file_path, 'w') as f:
            f.write(data)
    except Exception as e:
        raise Exception(f"Error writing SVG file: {str(e)}")