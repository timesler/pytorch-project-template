# pytorch-project-template

A template for building pytorch projects and packages.

```
pytorch_project_template
├── config.py            - File to define run parameters
├── data/                - Directory for data storage, data won't be tracked
├── dependencies/        - Directory for dependencies and submodules
├── docker-compose.yml   - Docker compose file
├── dockerfile           - Dockerfile with all dependencies
├── .dockerignore
├── environment.yml      - Conda environment file
├── .gitignore
├── __init__.py          - Defines project as a module
├── LICENSE              - MIT license
├── main.py              - Script that defines API routes (if using API)
├── models/              - Directory for pytorch modules
├── README.md
├── setup.py             - PyPI setup script, use for creating pip package
├── tests/
│   └── test.py          - Add some test code here, used by CI testing 
└── utils/                
    ├── datasets.py      - Custom datasets
    ├── samplers.py      - Custom samplers and batch samplers
    └── training.py      - Functions for training and evaluation
```

## Quick setup

Requires git, python, and conda.

1. Clone this project:
    ```bash
    git clone https://github.com/timesler/pytorch-project-template
    ```
1. Create a new project (see `create_project.py --help`):
    ```bash
    create_project.py <new_project_path> <new_project_owner>
    ```
    Optionally, the project can also include:
    * git: `--git`
    * docker and docker-compose to develop models in a container: `--docker`
    * a dockerfile and docker-compose service to serve models with a REST API: `--api`
    * a setup.py file for building a pip/PyPI package: `--pypi`
    * all of the above: `-full`
    
    E.g., for building a python package, you probably want:
    ```bash
    create_project.py <new_project_path> <new_project_owner> --git --pypi
    ```

1. Create development environment using conda or docker:
    * conda:
        ```bash
        conda create -n pytorch-py37 -f environment.yml
        conda activate pytorch-py37
        ```
    * docker/nvidia-docker:
        ```bash
        docker-compose run --rm train bash
        ```
1. (Optional) Deploy API for serving model:
    ```bash
    docker-compose up -d api
    ```

## Use as Github template

Alternatively, this repo can be used as a template for creating new repos on Github. Simply click "Use this template" at the top of the [main repo page](https://github.com/timesler/pytorch-project-template).

Following this, you should:

* Overwrite this README
* Remove the `create_project.py` utility
* Remove all unwanted files and folders
