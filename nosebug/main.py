# -*- coding: utf-8 -*-

from os import path


def main():
    return path.basename('/tmp/test.txt')


if __name__ == '__main__':
    print main()
