import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'django-cbvpatterns',
    version = '0.1',
    description = 'A better patterns() for classbased views',
    license = 'BSD',
    long_description = read('README.md'),
    url = 'https://github.com/lalzada/django-cbvpatterns',

    author = 'Lal Zada',
    author_email = 'lalzadamohmand@gmail.com',

    py_modules = ['cbvpatterns'],

    classifiers = (
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ),
)
