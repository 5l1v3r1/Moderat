from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.ini")
__all__ = [ basename(f)[:-4] for f in modules if isfile(f)]