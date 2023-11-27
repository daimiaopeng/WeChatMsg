import os

from app.decrypt import dat2pic
from app.person import MePC

if not os.path.exists('./data/image'):
    os.mkdir('./data/image')


def get_abs_path(path):
    # return os.path.join(os.getcwd(), 'app/data/icons/404.png')
    if path:
        # if os.path.exists(os.path.join())
        base_path = os.getcwd() + "/data/image"
        output_path = dat2pic.decode_dat(os.path.join(MePC().wx_dir, path), base_path) #'./data/image')
        return output_path
    else:
        return os.path.join(os.getcwd(), 'app/data/icons/404.png')
