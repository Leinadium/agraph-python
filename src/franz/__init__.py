# NOTE: Do *not* import any third-party libraries here,
# this will be included at setup time...
from __future__ import unicode_literals
import os.path
import pkg_resources
import re
import subprocess

# Determine version number

# Increment this whenever releasing a new Python Client
# for the same AG version, reset to 0 when new AG is released.
post_release = 0

__version__ = None

franz_dir = os.path.dirname(os.path.realpath(__file__))
path = os.path.normpath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'VERSION'))

# Try reading it from a VERSION file otherwise.
# It is generated by 'make dist' and included in the distribution.
try:
    with open(path, 'rb') as version_file:
        __version__ = version_file.read().strip().decode('ascii')
except IOError:
    pass

# Try asking setuptools...
if __version__ is None:
    try:
        __version__ = pkg_resources.require('agraph-python')[0].version
    except:   # A ton of different errors can be thrown by distutils...
        pass

# Otherwise assume we're inside agraph sources
if __version__ is None:
    agraph_root = os.path.normpath(os.path.join(franz_dir, '../../../agraph/lisp'))
    try:
        __version__ = subprocess.Popen(
            os.path.normpath(os.path.join(agraph_root, 
                                          'build-tools/agversion.sh')),
            cwd=agraph_root,
            stdout=subprocess.PIPE).communicate()[0].decode('ascii')
    except:
        # Use a default, print a warning
        print("WARNING: Unable to determine version, using 0.0.0")
        __version__ = '0.0.0'

__version__ = __version__.strip()

# Augment if necessary
if post_release:
    suffix = '.post%d' % post_release
    __version__ = re.sub('(\\.post[0-9]*)?$', suffix, __version__)
