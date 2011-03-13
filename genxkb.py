#!/usr/bin/python
# -*- coding: utf-8 -*-

keysym_map = {  # quoteright is a deprecated synonym
                # quoteleft is a deprecated synonym
                # Eth is a deprecated synonym
                # Oslash is a synonym
                # Thorn is a deprecated synonym
                # ooblique is a synonym
    ' ': ('space', '0x020'),
    '!': ('exclam', '0x021'),
    '"': ('quotedbl', '0x022'),
    '#': ('numbersign', '0x023'),
    '$': ('dollar', '0x024'),
    '%': ('percent', '0x025'),
    '&': ('ampersand', '0x026'),
    "'": ('apostrophe', '0x027'),
    '(': ('parenleft', '0x028'),
    ')': ('parenright', '0x029'),
    '*': ('asterisk', '0x02a'),
    '+': ('plus', '0x02b'),
    ',': ('comma', '0x02c'),
    '-': ('minus', '0x02d'),
    '.': ('period', '0x02e'),
    '/': ('slash', '0x02f'),
    ':': ('colon', '0x03a'),
    ';': ('semicolon', '0x03b'),
    '<': ('less', '0x03c'),
    '=': ('equal', '0x03d'),
    '>': ('greater', '0x03e'),
    '?': ('question', '0x03f'),
    '@': ('at', '0x040'),
    '[': ('bracketleft', '0x05b'),
    '\\': ('backslash', '0x05c'),
    ']': ('bracketright', '0x05d'),
    '^': ('asciicircum', '0x05e'),
    '_': ('underscore', '0x05f'),
    '`': ('grave', '0x060'),
    '{': ('braceleft', '0x07b'),
    '|': ('bar', '0x07c'),
    '}': ('braceright', '0x07d'),
    '~': ('asciitilde', '0x07e'),
    "¡": ('exclamdown', '0x0a1'),
    "¢": ('cent', '0x0a2'),
    "£": ('sterling', '0x0a3'),
    "¤": ('currency', '0x0a4'),
    "¥": ('yen', '0x0a5'),
    "¦": ('brokenbar', '0x0a6'),
    "§": ('section', '0x0a7'),
    "¨": ('diaeresis', '0x0a8'),
    "©": ('copyright', '0x0a9'),
    "ª": ('ordfeminine', '0x0aa'),
    "«": ('guillemotleft', '0x0ab'),
    "¬": ('notsign', '0x0ac'),
    "®": ('registered', '0x0ae'),
    "¯": ('macron', '0x0af'),
    "°": ('degree', '0x0b0'),
    "±": ('plusminus', '0x0b1'),
    "²": ('twosuperior', '0x0b2'),
    "³": ('threesuperior', '0x0b3'),
    "´": ('acute', '0x0b4'),
    "µ": ('mu', '0x0b5'),
    "¶": ('paragraph', '0x0b6'),
    "·": ('periodcentered', '0x0b7'),
    "¸": ('cedilla', '0x0b8'),
    "¹": ('onesuperior', '0x0b9'),
    "º": ('masculine', '0x0ba'),
    "»": ('guillemotright', '0x0bb'),
    "¼": ('onequarter', '0x0bc'),
    "½": ('onehalf', '0x0bd'),
    "¾": ('threequarters', '0x0be'),
    "¿": ('questiondown', '0x0bf'),
    "À": ('Agrave', '0x0c0'),
    "Á": ('Aacute', '0x0c1'),
    "Â": ('Acircumflex', '0x0c2'),
    "Ã": ('Atilde', '0x0c3'),
    "Ä": ('Adiaeresis', '0x0c4'),
    "Å": ('Aring', '0x0c5'),
    "Æ": ('AE', '0x0c6'),
    "Ç": ('Ccedilla', '0x0c7'),
    "È": ('Egrave', '0x0c8'),
    "É": ('Eacute', '0x0c9'),
    "Ê": ('Ecircumflex', '0x0ca'),
    "Ë": ('Ediaeresis', '0x0cb'),
    "Ì": ('Igrave', '0x0cc'),
    "Í": ('Iacute', '0x0cd'),
    "Î": ('Icircumflex', '0x0ce'),
    "Ï": ('Idiaeresis', '0x0cf'),
    "Ð": ('ETH', '0x0d0'),
    "Ñ": ('Ntilde', '0x0d1'),
    "Ò": ('Ograve', '0x0d2'),
    "Ó": ('Oacute', '0x0d3'),
    "Ô": ('Ocircumflex', '0x0d4'),
    "Õ": ('Otilde', '0x0d5'),
    "Ö": ('Odiaeresis', '0x0d6'),
    "×": ('multiply', '0x0d7'),
    "Ø": ('Ooblique', '0x0d8'),
    "Ù": ('Ugrave', '0x0d9'),
    "Ú": ('Uacute', '0x0da'),
    "Û": ('Ucircumflex', '0x0db'),
    "Ü": ('Udiaeresis', '0x0dc'),
    "Ý": ('Yacute', '0x0dd'),
    "Þ": ('THORN', '0x0de'),
    "ß": ('ssharp', '0x0df'),
    "à": ('agrave', '0x0e0'),
    "á": ('aacute', '0x0e1'),
    "â": ('acircumflex', '0x0e2'),
    "ã": ('atilde', '0x0e3'),
    "ä": ('adiaeresis', '0x0e4'),
    "å": ('aring', '0x0e5'),
    "æ": ('ae', '0x0e6'),
    "ç": ('ccedilla', '0x0e7'),
    "è": ('egrave', '0x0e8'),
    "é": ('eacute', '0x0e9'),
    "ê": ('ecircumflex', '0x0ea'),
    "ë": ('ediaeresis', '0x0eb'),
    "ì": ('igrave', '0x0ec'),
    "í": ('iacute', '0x0ed'),
    "î": ('icircumflex', '0x0ee'),
    "ï": ('idiaeresis', '0x0ef'),
    "ð": ('eth', '0x0f0'),
    "ñ": ('ntilde', '0x0f1'),
    "ò": ('ograve', '0x0f2'),
    "ó": ('oacute', '0x0f3'),
    "ô": ('ocircumflex', '0x0f4'),
    "õ": ('otilde', '0x0f5'),
    "ö": ('odiaeresis', '0x0f6'),
    "÷": ('division', '0x0f7'),
    "ø": ('oslash', '0x0f8'),
    "ù": ('ugrave', '0x0f9'),
    "ú": ('uacute', '0x0fa'),
    "û": ('ucircumflex', '0x0fb'),
    "ü": ('udiaeresis', '0x0fc'),
    "ý": ('yacute', '0x0fd'),
    "þ": ('thorn', '0x0fe'),
    "ÿ": ('ydiaeresis', '0x0ff'),
    "Ś": ('Sacute', '0x1a6'),
    "Ş": ('Scedilla', '0x1aa'),
    "Ź": ('Zacute', '0x1ac'),
    "ś": ('sacute', '0x1b6'),
    "ş": ('scedilla', '0x1ba'),
    "ź": ('zacute', '0x1bc'),
    "Ŕ": ('Racute', '0x1c0'),
    "Ĺ": ('Lacute', '0x1c5'),
    "Ć": ('Cacute', '0x1c6'),
    "Ń": ('Nacute', '0x1d1'),
    "ŕ": ('racute', '0x1e0'),
    "ĺ": ('lacute', '0x1e5'),
    "ć": ('cacute', '0x1e6'),
    "ń": ('nacute', '0x1f1'),
    }

keysyms = dict([(k.decode('utf-8'), v[0]) for (k, v) in keysym_map.iteritems()])
keycodes = dict([(k.decode('utf-8'), v[1]) for (k, v) in keysym_map.iteritems()])

from optparse import OptionParser
import sys
import re


def repl_keysym(match):
    ch = match.group(1)
    return keysyms.get(ch, ch)


def repl_keycode(match):
    ch = match.group(1)
    if ch >= '0' and ch <= '9':
        return '0x03' + ch
    if ch >= 'a' and ch <= 'z':
        return hex(0x61 + ord(ch) - ord('a'))
    return keycodes.get(ch, ch)


qwerty = ''.join(['`1234567890-=',
                  'qwertyuiop[]\\', 
                  'asdfghjkl;\'',
                  'zxcvbnm,./'])

def gen_map(mapto):
    buff = []
    keys = re.split('\s+', mapto)
    for i in xrange(0, min(len(mapto), len(qwerty))):
        qch = qwerty[i]
        tokey = keys[i]
        if qch == tokey:
            continue
        buff.append('keysym ')
        buff.append(keysyms.get(qch, qch))
        buff.append(' =')
        for key in tokey:
            buff.append(' ')
            buff.append(keysyms.get(key, key))
        buff.append('\n')
    return ''.join(buff)


def main():
    usage = \
        'usage: %prog [options] input\n $(char) = keysym, $c(char)=keycode'
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()
    if len(args) != 1:
        print parser.usage
        sys.exit(1)
    f = open(args[0])
    inmap = False
    buff = []
    for l in f:
        l = l.decode('utf-8')
        if inmap:
            if re.match('^\s*\$map\$\s*$', l):
                inmap = False
                sys.stdout.write(gen_map(' '.join(buff)))
                sys.stdout.write('! end map\n')
            else:
                buff.append(l)
                sys.stdout.write('! ' + l.encode('utf-8'))
        elif re.match('^\s*\$map\$\s*$', l):
            inmap = True
            sys.stdout.write('! begin map\n')
        else:
            l = re.sub(r'\$\((.)\)', repl_keysym, l)
            l = re.sub(r'\$c\((.)\)', repl_keycode, l)
            l = re.sub(r'\\\(', '(', l)
            l = re.sub(r'\\\$', '$', l)
            sys.stdout.write(l.encode('utf-8'))
    f.close()


if __name__ == '__main__':
    main()
