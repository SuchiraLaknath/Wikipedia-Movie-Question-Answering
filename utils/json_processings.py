

def get_nested(dictionary: dict, key: str, default=None, sep: str = "."):
    if sep in key:
        first_key, other_keys = key.split(sep, 1)
        return get_nested(dictionary.get(first_key, {}), other_keys, default)
    return dictionary.get(key, default)