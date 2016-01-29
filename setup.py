#!/usr/bin/env python
import sys

from setuptools import setup, find_packages

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
    readme = open('README.md').read()
    license = open('LICENSE').read()
elif PY3:
    readme = open('README.md', encoding='utf-8').read()
    license = open('LICENSE', encoding='utf-8').read()

setup(
    name='seqseek',
    version='0.1.4',
    url='https://github.com/23andMe/seqseek',
    download_url = 'https://github.com/23andMe/seqseek/tarball/0.1.4',
    author='23andMe Engineering',
    author_email=['jelofson@23andme.com', 'mstrand@23anmde.com'],
    description='Easy access to Build 37 & 38 human reference sequences',
    long_description=readme,
    entry_points={'console_scripts': [
            'download_build_37 = seqseek.downloader:cmd_line',
        ]},
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests'],
    classifiers=[
        #'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.4'
    ]
)
