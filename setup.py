"""
Flask-TemplateSupport
---------------------

Template support for flask application
"""

from setuptools import setup


with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='Flask-TemplateSupport',
    version='1.0.0',
    url='https://github.com/cs91chris/flask_template_support',
    license='MIT',
    author='cs91chris',
    author_email='cs91chris@voidbrain.me',
    description='Template support for flask application',
    long_description=long_description,
    packages=['flask_template_support'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask==1.0.2',
        'python-dateutil==2.8.0'
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
