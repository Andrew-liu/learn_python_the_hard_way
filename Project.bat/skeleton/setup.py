# -*- coding:utf-8 -*-

try :
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description' : 'My Project',
        'author' : 'Andrew_liu',
        'url' : 'https://github.com/Andrew-liu',
        'downlord' : 'git@github.com:Andrew-liu/LearningPython.git',
        'author_email' : 'liu.bin.coder@qq.com',
        'version' : '0.1',
        'install_requires' : ['nose'],
        'packages' : ['src'],
        'scripts' : [],
        'name' : 'projectname'
        }    

setup(**config)
