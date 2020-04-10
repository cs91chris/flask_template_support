"""
Flask-TemplateSupport
---------------------

Template support for flask application
"""
from setuptools import setup

from flask_template_support import author, __version__

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='Flask-TemplateSupport',
    version=__version__,
    url='https://github.com/cs91chris/flask_template_support',
    license='MIT',
    author=author['name'],
    author_email=author['email'],
    description='Template support for flask application',
    long_description=long_description,
    packages=['flask_template_support'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask==1.1.*',
        'python-dateutil==2.8.*'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
