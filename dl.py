__author__ = 'lazzzis'

import urllib.request
import sys
import re


def get_url_html(page):
    req = urllib.request.Request(page)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0")
    response = urllib.request.urlopen(req)
    return response.read()


def save_pic(filename, info):
    with open(filename, "wb") as f:
        f.write(info)


def get_pic_url(html):
    """This function is temporarily useless
    """
    p = re.compile('src="([^"]*)')
    return p.findall(p.findall(html))


def dl_pic(width, height, dir=''):
        html = get_url_html("http://placekitten.com/" + width + "/" + height)
        if html == b'':
            return False
            print("No such picture with the given size " + width + "*" + height)
        else:
            filename = dir + width + '-' + height + '.jpg' if len(sys.argv) < 4 else sys.argv[3]
            save_pic(filename, html)
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