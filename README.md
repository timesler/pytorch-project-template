# pytorch-project-template

A template for building pytorch projects and packages.

```
pytorch_project_template
├── config.py            - File to define run parameters
├── data                 - Directory for data storage, data won't be tracked
├── dependencies         - Directory for dependencies and submodules
├── docker-compose.yml   - Docker compose file
├── dockerfile           - Dockerfile with all dependencies
├── .dockerignore
├── environment.yml      - Conda environment file
├── .gitignore
├── __init__.py          - Defines project as a module
├── LICENSE              - MIT license
├── main.py              
├── models               - Directory for pytorch modules
├── README.md
├── setup.py             - PyPI setup script, use for creating pip package
├── tests
│   └── test.py          - Add some test code here, used by CI testing 
└── utils                
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
1. Create development environment using conda or docker:
    * conda:
        ```bash
        conda env create -f environment.yml
        conda activate pytorch-py37
        ```
    * nvidia-docker:
        ```bash
        docker-compose run --rm analytics bash
        ```
