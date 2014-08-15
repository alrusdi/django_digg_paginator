# -*- coding: utf-8 -*-
from distutils.core import setup

VERSION = "0.1.1"

setup(
    name = "django-digg-paginator",
    version = VERSION,
    packages = ["digg_paginator"],
    url = 'https://github.com/alrusdi/django_digg_paginator',
    author = 'Michael Elsdörfer',
    author_email = 'michael@elsdoerfer.com',
    maintainer = 'alrusdi',
    maintainer_email = 'alrusdi@gmail.com',
    license = 'GPL3',
    description = 'Digg-like Paginator from Django Snippets',
    long_description = open('README', 'r').read(),
    download_url = 'https://github.com/alrusdi/django_digg_paginator/archive/master.zip',
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',        
    ],
)
