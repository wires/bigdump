=======
Bigdump
=======

Simple python module for storing and retrieving lots of data on the filesystem.

Installation
============

Easiest using pip::

	pip install -e git+https://github.com/0x01/bigdump.git#egg=bigdump

Usage
=====

For example::

    >>> import bigdump
    >>> d = bigdump.Bigdump('my_data')

    >>> d.store('banana', [1,2,{'a':'b'}])
    >>> d.store('cookie', {'d': ["c",34]})

    >>> d.retrieve('banana')
    [1, 2, {'a': 'b'}]

This will store the files in `./my_data/`. The keys are MD5 hashed and
converted into a filesystem path. The value is then pickled into that file::

    my_data
    |-- 2
    |   `-- d
    |       `-- c
    |           `-- c
    |               `-- d
    |                   `-- 1
    |                       `-- ab3e03990aea77359831c85ca2
    `-- 7
        `-- 2
        `-- b
            `-- 3
            `-- 0
                `-- 2
                `-- bf297a228a75730123efef7c41

    12 directories, 2 files

You can easily get all documents in the dump::

    >>> list(d.all())
    [{'d': ['c', 34]}, [1, 2, {'a': 'b'}]]

But don't use list() with a big dump, because it is constructed in memory.  It
is better to use a loop::

    # d.all() is an iterator
    for doc in d.all():
        # do something with doc
        print doc

Have fun!


