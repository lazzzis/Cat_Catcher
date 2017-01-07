__author__ = 'lazzzis'

import argparse
from contextlib import contextmanager
from os import chdir, getcwd

import requests
from requests.exceptions import RequestException


def save_pic(filename, info):
    """save the picture to the current directory"""
    with open(filename, "wb+") as pic:
        pic.write(info)


def pic_url(width, height):
    """Return the url for the specific size of pic

    >>> pic_url(200, 300)
    'http://placekitten.com/200/300'

    >>> pic_url(10000, 0)
    'http://placekitten.com/10000/0'

    >>> pic_url(0, 100)
    'http://placekitten.com/0/100'
    """
    return "http://placekitten.com/{width}/{height}".format(
        width=width, height=height)


def dl_pic(width, height, filename):
    """downloaded the picture with given size and filename"""
    if width < 0 or height < 0:
        raise ValueError("Positive integer is required to download picture")

    response = requests.get(pic_url(width, height))
    if response.content == b'':
        raise RequestException(
            "No such picture with the given size {width} * {height}".format(
                width=width, height=height))

    filename = filename or "{width}-{height}.jpg".format(
        width=width, height=height)

    save_pic(filename, response.content)

    print("The picture is downloaded successfully!")
    return True


def make_parser():
    """Make a argument parser for analyzing two required arguments -- width, length"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'width', type=int, help="an integer indicating the width")
    parser.add_argument(
        'height', type=int, help="an integer indicating the height")
    parser.add_argument(
        '--path',
        '-p',
        type=str,
        default='.',
        help="the path storing the pictore")
    parser.add_argument(
        '--name', '-n', type=str, default='', help="the picture name")

    return parser


@contextmanager
def change_dir(target_path):
    """A function assisting change working directory temporarily

    >>> import os
    >>> os.chdir(os.path.expanduser('~'))
    >>> os.getcwd() == os.path.expanduser('~')  # You're in your home directory now
    True
    >>> with change_dir('/usr/local'): # change working directory to '/usr/local'
    ...     print(os.getcwd())
    ...     pass # Anything you want to do in this directory
    ...
    /usr/local
    >>> os.getcwd() == os.path.expanduser('~') # You're back in your previous working directory
    True

    """
    current_path = getcwd()
    chdir(target_path)
    yield
    chdir(current_path)


def main():
    parser = make_parser()
    args = parser.parse_args()
    with change_dir(args.path):
        dl_pic(args.width, args.height, args.name)

if __name__ == '__main__':
    main()
