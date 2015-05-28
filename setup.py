print '''
Installing template....                                        

'''

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import versioneer
import sys


config = {
    'description': 'Template is a simple example python package',
    'author': 'Anmol Garg',
    'url': 'here',
    'download_url': 'Where to download it.',
    'author_email': 'anmolgarg314@gmail.com',
    'version': versioneer.get_version(),
    'cmdclass': versioneer.get_cmdclass(),
    
    'install_requires': [
    'numpy',
    'pandas',
    'nose',
    ],
    'packages': find_packages(),
    'scripts': [],
    'name': 'template'
}

print "system is: "+sys.platform
print '\n'
print "installing stencil dependencies... "
print config['install_requires']

setup(**config)