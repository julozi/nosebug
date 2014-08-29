# -*- coding: utf-8 -*-

from unittest import TestCase

from nosebug.main import main


class MainTest(TestCase):

    def test_main(self):
        self.assertEqual(main(), u"test.txt")
