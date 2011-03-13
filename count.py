#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from os.path import join

INCLUDE_EXT = (  # 'html',
    'py',
    'java',
    'c',
    'h',
    'cc',
    'hh',
    'hpp',
    'cpp',
    'rb',
    'sh',
    'txt',
    'yaml',
    'css',
    'js',
    'xml',
    'json',
    'ini',
    'sql',
    'properties',
    )
IGNORE_DIR = (r'^\..*', 'cvs', 'eric', '.*-build')


class ZeroDict(dict):

    def __getitem__(self, k):
        return self.get(k, 0)


isblank = lambda c: c == ' ' or c == '\t' or c == '\n'


class Statistic:

    def __init__(self):
        self.char1_stat = ZeroDict()
        self.caps_stat = ZeroDict()
        self.char2_stat = ZeroDict()
        self.char3_stat = ZeroDict()
        self.word_stat = ZeroDict()
        self.path = None
        self.include = [k for k in INCLUDE_EXT]

    def add_char(self, c):
        if ord(c) > 64 and ord(c) < 91:
            self.caps_stat[c] += 1
        self.char1_stat += 1

    def add_word(self, w):
        for i in xrange(0, len(w) - 2):
            self.add_char(w[i])
            self.char2_stat[w[i:i + 1]] += 1
            self.char3_stat[w[i:i + 2]] += 1
        self.add_char(w[len(w) - 1])
        self.word_stat[w.lower()] += 1

    def add_text(self, text):
        for i in xrange(0, len(text)):
            if isblank(text[i]):
                continue
            self.char1_stat[text[i]] += 1
            self.char1_stat['count'] += 1
            if i > len(text) - 2 or isblank(text[i + 1]):
                continue
            self.char2_stat[text[i:i + 2]] += 1
            self.char2_stat['count'] += 1
            if i > len(text) - 3 or isblank(text[i + 2]):
                continue
            self.char3_stat[text[i:i + 3]] += 1
            self.char3_stat['count'] += 1

    def count_file(self, filename, pinyin=False):
        print filename
        for line in open(filename):
            if pinyin:
                line = line.decode('utf-8')
                from pinyin import zh2pinyin8char
                line = zh2pinyin8char(line)
            self.add_text(line.lower())

    def count_dir(self, path, pinyin=False):
        import os
        self.path = path

        for (root, dirs, files) in os.walk(path, followlinks=True):
            print root, '\n'
            for f in files:
                for ext in self.include:
                    if f.endswith('.' + ext):
                        self.count_file(join(root, f), pinyin)
                        break
            for d in dirs:
                for ignore_dir in IGNORE_DIR:
                    if re.match(ignore_dir, d):
                        dirs.remove(d)
                        break

    def __str__(self):
        return """chars: %s
        char2: %s
        char3: %s""" \
            % (str(self.char1_stat), str(self.char2_stat),
               str(self.char3_stat))


def write_data(data, out):
    count = float(data['count'])
    l = [(k, v) for (k, v) in data.iteritems()]
    l = sorted(l, key=lambda k: k[1], reverse=True)[:200]
    for v in l:
        try:
            k = v[0].encode('utf-8')
        except:
            k = v[0]
        out.write('%s\t%s\t%.2f%%\n' % (k, v[1], v[1] / float(count)
                  * 100))


def save_data(data, filename):
    f = open(filename, 'w')
    write_data(data, f)
    f.close()


def main():
    stat = Statistic()
    stat.count_dir('/home/gl/abs')
    save_data(stat.char1_stat, 'apps/char1_stat.out')
    save_data(stat.char2_stat, 'apps/char2_stat.out')
    save_data(stat.char3_stat, 'apps/char3_stat.out')


if __name__ == '__main__':
    main()
