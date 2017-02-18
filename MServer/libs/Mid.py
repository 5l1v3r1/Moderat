import string, random


def generateMid(size=24, chars=string.digits):
    random_chars = ''.join(random.choice(chars) for _ in range(size))
    h = hex(int(random_chars))[2:].zfill(12)
    return ":".join(i + j for i, j in zip(h[::2], h[1::2]))