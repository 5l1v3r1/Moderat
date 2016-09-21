import urllib
import sys
import os
import zipfile

site_packages = os.path.join(os.path.dirname(sys.argv[0]), 'packages')
if not os.path.exists(site_packages):
    os.makedirs(site_packages)
open(os.path.join(site_packages, '__init__.py'), 'w').close()
sys.path.insert(1, site_packages)
url = r'https://pypi.python.org/packages/9c/32/004ce0852e0a127f07f358b715015763273799bd798956fa930814b60f39/pip-8.1.2-py2.py3-none-any.whl'
try:
    urllib.urlretrieve(url, "pip.whl")
except IOError:
    pass
fh = open('pip.whl', 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    z.extract(name, site_packages)
fh.close()