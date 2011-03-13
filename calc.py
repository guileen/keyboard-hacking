#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from count import ZeroDict, save_data
from os.path import join


def load_data(filename):
    print filename
    f = open(filename)
    data = ZeroDict()
    for line in f:
        matcher = re.match(r"(\S+)\s+(\d+)\s.*", line)
        if matcher:
            data[matcher.group(1)] = int(matcher.group(2))
    return data


def powerstat(root, filename, powers):
    stat = ZeroDict()
    base = 100000
    for (_dir, power) in powers.iteritems():
        data = load_data(join(root, _dir, filename))
        count = data['count']
        print count
        if count == 0:
            continue
        powered_count = power * base
        print 'powered_count', powered_count
        powered_base = powered_count / float(count)
        for (k, v) in data.iteritems():
            powered_value = powered_base * v
            print k, v, powered_value
            if k[0] > k[len(k) - 1]:
                k = k[::-1]
            stat[k] += powered_value
    return stat


def main():
    powers = {
        'java': 0.5,
        'android': 0.5,
        'py': 1,
        'apps': 1,
        'ruby': 1,
        'shell': 1,
        'js': 1,
        'php': 1,
        }
    stat = powerstat('.', 'char1_stat.out', powers)
    save_data(stat, 'char1_stat.out')
    stat = powerstat('.', 'char2_stat.out', powers)
    save_data(stat, 'char2_stat.out')
    stat = powerstat('.', 'char3_stat.out', powers)
    save_data(stat, 'char3_stat.out')


if __name__ == '__main__':
    main()
