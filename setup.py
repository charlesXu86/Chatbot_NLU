# -*- coding: utf-8 -*-

'''
@Author  :   Xu

@Software:   PyCharm

@File    :   set_up.py

@Time    :   2019-06-06 16:22

@Desc    :   setup

'''
from setuptools import find_packages, setup, convert_path
import pathlib

def _version():
    ns = {}
    with open(convert_path("chatbot_nlu/version.py"), "r") as fh:
        exec(fh.read(), ns)
    return ns['__version__']

__version = _version()

# Package meta-data.
NAME = 'chatbot-nlu'
DESCRIPTION = 'nlu of classifiers detection、name entity recognition、classification of chinese text'
URL = 'https://github.com/charlesXu86/Chatbot_NLU'
EMAIL = 'charlesxu86@163.com'
AUTHOR = 'xu'
LICENSE = 'MIT'

HERE = pathlib.Path(__file__).parent
with open("README.rst", "r") as fh:
    long_description = fh.read()

required = [
            'bert-serving-client==1.8.9',
            'bert-serving-server==1.9.2',
            ]

setup(
    name=NAME,
    version=__version,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    package_data={'chatbot_nlu': ['resource/*.json', '*.rst']},
    install_requires=required,
    license=LICENSE,
    classifiers=['License :: OSI Approved :: MIT License',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8',
                     'Programming Language :: Python :: Implementation :: CPython',
                     'Programming Language :: Python :: Implementation :: PyPy'],)
print("Welcome to Chatbot_NLU, and Chatbot_NLU version is {}".format(__version))
