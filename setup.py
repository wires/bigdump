from distutils.core import setup

setup(
    name='BigDump',
    version='0.1.0',
    author='J. Herold',
    author_email='jelle@defekt.nl',
    packages=['bigdump',],
    scripts=[],
    url='https://github.com/0x01/bigdump',
    license='LICENSE.txt',
    description='Store a lot of data on the filesystem',
    long_description=open('README.txt').read()
)
