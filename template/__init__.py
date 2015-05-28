'''
provides __version__ module attribute

'''
import stencil
import submodule

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
