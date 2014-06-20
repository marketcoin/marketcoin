import os

basedir = os.path.join(os.path.expanduser('~'), '.marketcoin')

if not os.path.exists(basedir):
    os.mkdir(basedir)

_open = open
def open(filename, *args, **kwargs):
    filename = os.path.join(basedir, filename)
    if not os.path.exists(filename):
        _open(filename, 'a').close()
    return _open(filename, *args, **kwargs)