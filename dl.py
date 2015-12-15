__author__ = 'lazzzis'

import requests
import sys
import re
import os.path


def save_pic(filename, info):
    with open(filename, "wb") as f:
        f.write(info)


def get_pic_url(html):
    """This function is temporarily useless
    """
    p = re.compile('src="([^"]*)')
    return p.findall(p.findall(html))


def dl_pic(width, height, dir=''):
    try:
        r = requests.get("http://placekitten.com/" + width + "/" + height)
    except:
        print("No such picture with the given size " + width + "*" + height)
        return False
    filename = os.path.join(dir, width + '-' + height + '.jpg') if len(sys.argv) < 4 else sys.argv[3]
    save_pic(filename, r.content)
    print("The picture is downloaded successfully!")
    return True


"""3 arguments are needed
The first one and second one are the width and height of the picture respectively
The third one is the filename and this is optional. If the second one is not provided, the pic will save on the current
folder
"""
if __name__ == '__main__':
    try:
        width, height = sys.argv[1], sys.argv[2]
        dl_pic(width, height)
    except IndexError:
        print("The program can't work because it need at lease two argumentss!")
