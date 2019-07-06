import argparse
import os
import subprocess
import shutil

# TODO: Add flags to control project functionality (docker, setup, license, travis-ci)

DESCRIPTION = """Create pytorch project template.

A clone of this project will be created at the specified path (e.g., '../new_project'). Everything
from the current project is copied except for the .git/ directory and this script. The resulting
project will be an initialized git repository with an MIT license. The LICENSE file is modified to
reference the specified project owner.
"""


def create_project(path, owner):
    # Don't proceed if path already exists
    if os.path.exists(path):
        raise Exception(f'Path ({path}) already exists. Remove the target directory or choose '
            'another location.')
    
    # Make project directory and initialize it as a git repo
    os.makedirs(path)
    subprocess.call(['git', 'init'], cwd=path)
    
    # Loop through items in template, skipping .git/ and this file
    for d in os.listdir('.'):
        if d != '.git' and d != __file__:
            if os.path.isdir(d):
                shutil.copytree(d, os.path.join(path, d))
            if os.path.isfile(d):
                shutil.copyfile(d, os.path.join(path, d))
    
    # Modify LICENSE file to have the correct owner for the project
    subprocess.call(['sed', '-i', f's/Tim Esler/{owner}/g', os.path.join(path, 'LICENSE')])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('path', type=str, help='Path to directory of new project.')
    parser.add_argument('owner', type=str, help='Name of project owner for the license file.')
    args = parser.parse_args()

    print(f'Creating new project at {args.path}, owned by {args.owner}')

    create_project(args.path, args.owner)
