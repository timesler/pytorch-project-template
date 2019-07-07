import argparse
import os
import subprocess
import shutil
import glob

# TODO: Add travis-ci

DESCRIPTION = """Create pytorch project template.

A clone of this project will be created at the specified path (e.g., '../new_project'). Everything
from the current project is copied except for the .git/ directory and this script. The LICENSE
file is modified to reference the specified project owner.

A number of flags are used to control what is copied into the new project, which can optionally
include (1) git, initialized before adding new files; (2) docker and docker-compose; and (3) a
dockerfile and docker-compose service for model deployment via a REST API. 
"""


def create_project(path, owner, full, git, docker, api):
    # Don't proceed if path already exists
    if os.path.exists(path):
        raise Exception(f'Path ({path}) already exists. Remove the target directory or choose '
            'another location.')
    
    # Make project directory and initialize it as a git repo
    os.makedirs(path)
    if git:
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

    # Full project structure
    if full:
        return
    # Without git
    if not git:
        git_files = glob.glob(f'{path}/**/.git*')
        for f in git_files:
            os.remove(f)
    # Without api
    if not docker or not api:
        os.remove(os.path.join(path, 'docker/api.dockerfile'))
        dc = os.path.join(path, 'docker-compose.yml')
        subprocess.call(['sed',  '-i', '/api/Q', os.path.join(path, 'docker-compose.yml')])
    # Without docker
    if not docker:
        os.remove(os.path.join(path, '.dockerignore'))
        os.remove(os.path.join(path, 'docker-compose.yml'))
        shutil.rmtree(os.path.join(path, 'docker'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('path', type=str, help='Path to directory of new project.')
    parser.add_argument('owner', type=str, help='Name of project owner for the license file.')
    parser.add_argument('--full', action='store_true', help='Whether to include full structure (base+docker+api+CI).')
    parser.add_argument('--git', action='store_true', help='Whether to include git.')
    parser.add_argument('--docker', action='store_true', help='Whether to include docker and docker-compose.')
    parser.add_argument('--api', action='store_true', help='Whether to include REST API for serving models.')
    args = parser.parse_args()

    print(f'Creating new project at {args.path}, owned by {args.owner}')

    create_project(
        args.path,
        args.owner,
        args.full,
        args.git,
        args.docker,
        args.api,
    )
