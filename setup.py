import os
from setuptools import setup

#README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mezzanine_advanced_pages',
    version='0.1',
    packages=['mezzanine_advanced_pages'],
    include_package_data=True,
    license='BSD License',
    description='Blockable pages and layout for Mezzanine CMS',
    long_description=README,
    url='http://www.evolutionwebsolutions.com/',
    author='Nick Lyga',
    author_email='nick@evolutionwebsolutions.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Mezzanine',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    requires=['mezzanine_blocks'],
)