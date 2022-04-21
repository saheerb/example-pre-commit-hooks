#!/usr/bin/env python3
#
# Copyright (c) 2019-2021, Arm Limited. All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause
#

import argparse
import os
import re
import sys
import hooks.utils


def parse_cmd_line():
    parser = argparse.ArgumentParser(
        description="Check Banned APIs",
        epilog="""
            For each source file in the tree, checks whether Banned APIs as
            described in the list are used or not.
        """
    )

    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument("--verbose", "-v",
                        help="Print verbose output",
                        action="store_true")
    args = parser.parse_args()
    return args

def main():
    args = parse_cmd_line()

    print(args)

if __name__ == '__main__':
    raise SystemExit(main())
