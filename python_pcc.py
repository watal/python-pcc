#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import sys
import segmentlist_sockcli


def main(src, dst):
    '''simple pcc for FRRouting'''

    segmentlist_sockcli.ssocket((src, dst))

    return 0


if __name__ == '__main__':
    '''check args'''
    argv = sys.argv
    if len(argv) != 3:
        print('Usage: python {} [source] [destination]'.format(argv[0]), file=sys.stderr)
        quit()

    main(argv[1], argv[2])
