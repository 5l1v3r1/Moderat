# coding=utf-8
_ = {
    'a': u'ა',
    'b': u'ბ',
    'g': u'გ',
    'd': u'დ',
    'e': u'ე',
    'v': u'ვ',
    'z': u'ზ',
    'T': u'თ',
    'i': u'ი',
    'k': u'კ',
    'l': u'ლ',
    'm': u'მ',
    'n': u'ნ',
    'o': u'ო',
    'p': u'პ',
    'J': u'ჟ',
    'r': u'რ',
    's': u'ს',
    't': u'ტ',
    'u': u'უ',
    'f': u'ფ',
    'q': u'ქ',
    'R': u'ღ',
    'y': u'ყ',
    'S': u'შ',
    'C': u'ჩ',
    'c': u'ც',
    'Z': u'ძ',
    'w': u'წ',
    'W': u'ჭ',
    'x': u'ხ',
    'j': u'ჯ',
    'h': u'ჰ',
}

all_ = open('2.py', 'r').read()

for latin, sylfaen in _.items():
    all_ = all_.replace(latin, sylfaen)

with open('3.py', 'w') as _file:
    _file.write(all_.encode('utf-8'))

