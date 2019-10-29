#!/usr/bin/env python
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : setup.py
#   Created Time  : 2019-09-24 10:51
#   Last Modified : 2019-10-16 21:03
#   Describe      :
#
# ====================================================

from setuptools import setup
from setuptools import find_packages
# import sys
# import os
import core
setup(
    name='SmartHepSub',
    version='1.0',
    author='Xin-Xin Ma',
    packages=find_packages(),
    project_urls={
    'Source': 'https://github.com/xxmawhu/SmartHepSub',
	},  
    entry_points={
        'console_scripts':[
            'hep.sub=smartHepsub.hepsub:main',
            ]
        },
    install_requires=[
        'termcolor',
        'progressbar',
        ]
)
