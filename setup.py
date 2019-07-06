import setuptools, os

PACKAGE_NAME = ''
VERSION = ''
AUTHOR = ''
EMAIL = ''
DESCRIPTION = ''
GITHUB_URL = ''

parent_dir = os.path.dirname(os.path.realpath(__file__))
import_name = os.path.basename(parent_dir)

with open(f'{parent_dir}/README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=GITHUB_URL,
    packages=[
        f'{import_name}',
        f'{import_name}.models',
        f'{import_name}.utils',
   ],
    package_data={'': []},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)