#!/usr/bin/env python3

import os
import re
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        required=True,
                        type=str,
                        action='store',
                        metavar='PATH',
                        help="Path to the markdown file"
                        )
    parser.add_argument('-d', '--depth',
                        default=2,
                        type=int,
                        action='store',
                        metavar='DEPTH',
                        help="Up to which heading depth the TOC should be created: 0 = #, 1 = ##...")
    args = parser.parse_args()

    if not os.path.isfile(args.file) or not args.file.lower().endswith('.md'):
        sys.exit("File could not be found or the file type is incorrect!")

    toc = []

    with open(args.file) as file:
        for line in file:
            if line.startswith('#'):
                depth = line.count('#') - 1

                if depth <= args.depth:
                    f_line = re.sub('[^.a-z\d\s-]', '', line.lower())
                    f_line = f_line.strip().replace(' ', '-')
                    f_line = re.sub('-+', '-', f_line)

                    link = '{}- [{}](#{})'.format('  ' * depth, line.replace('#', '').strip(), f_line)
                    toc.append(link)

    for link in toc:
        print(link)


if __name__ == '__main__':
    main()
