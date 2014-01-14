import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='playdj',
    version='0.1',
    packages=['playdj'],
    include_package_data=True,
    license='MIT License',  # example license
    description='A music queueing service for Google Music.',
    url='http://playdj.io',
    author='Nick Depinet & Julien Eid',
    author_email='nick@csh.rit.edu',
    long_description=README,
    install_requires = ["django"],
    classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Programming Language :: Python',
            # Replace these appropriately if you are stuck on Python 2.
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)
