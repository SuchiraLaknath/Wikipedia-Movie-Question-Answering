import base64, os
from groq import Groq
from datetime import datetime, timezone
import platform

def b64(path):
    return base64.b64encode(open(path, "rb").read()).decode("utf-8")


def get_fs_times(path):
    st = os.stat(path)
    # Modified time (all platforms)
    mtime = datetime.fromtimestamp(st.st_mtime).isoformat()

    return mtime


def read_images(images_dir_path):
    pngs = []
    story_dir = images_dir_path
    names =  os.listdir(story_dir)
    names = sorted(names)
    for name in names:
        path = os.path.join(story_dir, name)
        if os.path.isfile(path) and os.path.splitext(name)[1].lower() == ".png":
            frame_id=name
            timestamp = get_fs_times(path= path)
            b64_image_str = b64(path= path)
            image_info = {
                "frame_id":frame_id,
                "timestamp":timestamp,
                "base64_string":b64_image_str
            }
            pngs.append(image_info)
    return pngs