#!/usr/bin/python
# -*- coding: utf-8 -*-

from optparse import OptionParser
import sys
from count import write_data
from count import Statistic


def main():
    usage = \
        'python keystat.py [-f file][-d dir][-z|--pinyin][-r][-o dir][-i extension][-x exclude]'
    parser = OptionParser(usage)

    parser.add_option('-d', '--dir', dest='directory',
                      help='count letters in directory')
    parser.add_option('-f', '--file', dest='filename',
                      help='count letters in directory')
    parser.add_option(
        '-z',
        '--pinyin',
        dest='pinyin',
        action='store_true',
        help='convert chinese to pinyin',
        default=False,
        )
    parser.add_option(
        '-r',
        '--recursion',
        dest='recursion',
        action='store_true',
        help='count subdirectories',
        default=True,
        )
    parser.add_option('-o', '--outdir', dest='outdir',
                      help='out put file, stdout default', default=None)
    parser.add_option('-i', '--include', dest='include',
                      help='include extension')
    parser.add_option('-x', '--exclude', dest='exclude',
                      help='exclude extension')
    (options, args) = parser.parse_args()

    stat = Statistic()
    if options.include:
        stat.include.append(options.include)

    if options.exclude:
        stat.include.remove(options.exclude)

    if options.filename:
        stat.count_file(options.filename, options.pinyin)
    if options.directory:
        stat.count_dir(options.directory, options.pinyin)
        if not options.outdir:
            options.outdir = options.directory

    if not options.filename and not options.directory:
        print parser.usage
        sys.exit(1)

    from os.path import join
    if options.outdir:
        out1 = open(join(options.outdir, 'char1_stat.out'), 'w')
        out2 = open(join(options.outdir, 'char2_stat.out'), 'w')
        out3 = open(join(options.outdir, 'char3_stat.out'), 'w')
    else:
        out1 = out2 = out3 = sys.stdout

    write_data(stat.char1_stat, out1)
    write_data(stat.char2_stat, out2)
    write_data(stat.char3_stat, out3)

    if options.outdir:
        out1.close()
        out2.close()
        out3.close()


if __name__ == '__main__':
    main()
