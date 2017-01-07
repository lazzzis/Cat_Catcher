import os
import unittest

from dl import *


class ParserTest(unittest.TestCase):
    def test_parser_width_height_str(self):
        parser = make_parser()
        self.assertRaises(SystemExit, parser.parse_args, ["123", "45e"])
        self.assertRaises(SystemExit, parser.parse_args, ["12e", "45e"])
        self.assertRaises(SystemExit, parser.parse_args, ["12e", "45"])

    def test_parser_no_arg(self):
        parser = make_parser()
        self.assertRaises(SystemExit, parser.parse_args, [])


class Dl_PC_Test(unittest.TestCase):
    def tearDown(self):
        if os.path.exists("test.jpg"):
            os.remove("test.jpg")

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            dl_pic(-100, 100, 'test.jpg')
        with self.assertRaises(AssertionError):
            with self.assertRaises(ValueError):
                dl_pic(1200, 900, 'test.jpg')

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            dl_pic(100, -100, 'test.jpg')
        with self.assertRaises(Exception):
            with self.assertRaises(ValueError):
                dl_pic(1200, 900, 'test.jpg')

    def test_success_dl(self):
        dl_pic(1200, 900, "test.jpg")
        self.assertTrue(os.path.exists("test.jpg"))
