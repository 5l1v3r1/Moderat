import os, random, string


def idGenerator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def getFlag(moderat, country_code):
    flags_dir = os.path.join(moderat.BASEDIR, 'assets', 'flags')
    try:
        country_flag = os.path.join(flags_dir, country_code.lower() + '.png')
        if os.path.exists(country_flag):
            return country_flag
        else:
            return os.path.join(flags_dir, 'blank.png')
    except:
        return os.path.join(flags_dir, 'blank.png')