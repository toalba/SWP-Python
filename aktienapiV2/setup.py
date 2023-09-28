from setuptools import find_packages
from setuptools import setup
from setuptools.command.test import test
import os


def read_file(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read()


version = '0.3.dev0'
shortdesc = 'alphavantage aktien api'
longdesc = ''

setup(
    name='aktien.alphavantage',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords='aktien alphavantage finance finanzen',
    author='toalba',
    author_email='',
    url='https://github.com/toalba/SWP-Python',
    license='GPL 3.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['aktien'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
)