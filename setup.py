#!/usr/bin/env python

from distutils.core import setup

setup(name='SeenThis',
      version='0.0',
      description='Use the SeenThis API',
      long_description='Use the SeenThis API. SeenThis <http://seenthis.net> is a social network mostly targeted towards the exchange of interesting URLs and short-blogging. See the source code and the example scripts for documentation.',
      license='BSD',
      author='Stephane Bortzmeyer',
      author_email='stephane+seenthis@bortzmeyer.org',
      url='https://github.com/bortzmeyer/seenthis-python',
      download_url='https://github.com/bortzmeyer/seenthis-python/tarball/master',
      py_modules=['SeenThis', 'FeedParserPlus'],
      scripts=['seenthis-backup.py', 'seenthis-post.py'],
      data_files=[('/usr/local/doc/SeenThis', ['README',]),],
      provides=['SeenThis',],
      requires=['TODO_seems_completely_ignored', 'feedparser']
      )
# TODO: add classifiers
