# Scientific Project Organization Framework

[简体中文](README_CN.md)

A complete scientific project involves multiple aspects such as data, code, and reports. Properly organizing these components facilitates project management, reproducibility, backup, and traceability.  
Based on practical experience, this document presents a project organization framework inspired by [Mario Krapp/semic-project](https://gitlab.pik-potsdam.de/krapp/semic-project) and [Joshua Cook](https://joshuacook.netlify.app/posts/2024-07-27_python-data-analysis-org/).  
Using the `cookiecutter` tool, you can quickly generate [the framework structure as shown below](#project-structure) and easily start a new scientific project.

## Quick Start

```shell
pip install cookiecutter
cookiecutter https://github.com/Mingzefei/cookiecutter-science.git
```

## Project Structure

```text
.
├── AUTHORS.md                      <- Project authorship information
├── LICENSE                         <- Project's open source license
├── README.md                       <- Project description, including an overview and installation instructions
├── backup                          <- Backup folder for storing configuration and result backups, not tracked by version control
├── config                          <- Directory for configuration files
│   └── config.yaml                 <- Main configuration file, including computation parameters and settings
├── data                            <- Directory for data used in the project, not tracked by version control
│   ├── external                    <- External datasets, such as validation or comparison data from other research teams
│   ├── interim                     <- Intermediate data, processed for further analysis or exploration
│   ├── processed                   <- Final processed datasets, ready for modeling and analysis
│   └── raw                         <- Original raw data, untouched
├── docs                            <- Documentation, including technical documents and research papers
├── notebooks                       <- Contains Jupyter Notebooks for early-stage exploration, code experimentation, and demonstration
│   └── 00_draft_example.ipynb      <- Example notebook, used as a draft
├── pyproject.toml                  <- Project configuration file for dependencies and packaging
├── reports                         <- Contains reports and related content
│   ├── Makefile                    <- Makefile for compiling LaTeX reports
│   ├── archive                     <- Folder for storing archived drafts
│   ├── figures                     <- Figures and images for the reports
│   ├── main.tex                    <- Main LaTeX report file
│   └── si.tex                      <- Supplementary information in LaTeX format
├── results                         <- Directory for experiment and analysis results, not tracked by version control
├── scripts                         <- Various executable scripts for downloading data, cleaning, backing up results, etc.
│   ├── __init__.py                 <- Initialization file for the scripts module
│   ├── backup.py                   <- Script for backing up data
│   ├── clean.py                    <- Script for data cleaning
│   ├── config_loader.py            <- Script for loading configuration files
│   ├── data_downloader.py          <- Script for downloading data
│   └── paths.py                    <- Script for defining project paths and folder locations
└── {{cookiecutter.project_slug}}   <- Core project code (referred to as `src`), can be packaged as an independent Python package
    ├── __init__.py                 <- Initialization file for the project package
    ├── cli.py                      <- Command-line interface for core project functionalities
    ├── data                        <- Logic for data processing
    │   ├── __init__.py             
    │   └── clean_data.py           <- Logic for data cleaning
    ├── external                    <- External libraries or code, not tracked by version control
    ├── models                      <- Code for model building and training
    │   └── __init__.py             
    ├── plot                        <- Logic for data visualization
    │   ├── __init__.py             
    │   └── plot_style.py           <- Script for defining data visualization styles
    └── utils                       <- Utility functions, including file I/O, logging, and other auxiliary functionalities
        ├── __init__.py             
        ├── file_io.py              <- File input/output logic
        └── logger.py               <- Logging logic
```

### Explanation

(The core project code, `{{cookiecutter.project_slug}}`, is referred to as `src` below)

1. `src` contains the core code, with input/output abstracted as data structures rather than specific files or paths. It can be published as an independent package.
    - `src/data`: Logic for data processing.
    - `src/utils`: Utility functions and helper classes, such as file I/O and logging.
    - `src/models`: Logic for model building and classes.
    - `src/plot`: Logic for data visualization.
2. `scripts` contains executable scripts for tasks such as data downloading, model training, and result backup. These scripts can call `scripts/paths.py`, `scripts/config_loader.py`, and `src` to access paths, configurations, and core code logic.
    - `scripts/paths.py`: Defines folder paths for the project, usually fixed.
    - `scripts/config_loader.py`: Loads the project configuration file for specifying experimental parameters, which can be modified as needed.
3. `notebooks` contains all Jupyter Notebook files, used initially for quick prototyping and exploration, and later for execution and presentation.
    - It's recommended to regularly encapsulate code from `notebooks` into `src` and `scripts` to keep notebook files clean and enable automation.
    - Jupyter Notebook files should follow the naming convention `<incremental_number>_<descriptive_name>.ipynb`, such as `01_data_process.ipynb`. The `<incremental_number>` is a two-digit format `xy`, where `y` increments and `x` has the following meaning:
        - 0: Draft
        - 1: Data
        - 2: Model
        - 3: Results (e.g., visualization)
        - 4: Report
4. `docs` stores project-related literature and technical documentation.
5. `reports` contains the final project reports (e.g., LaTeX files) and archived drafts (e.g., md, docx, pptx, pdf).
6. `data` stores the project data files, which are often large and not tracked by version control.
    - `data/raw`: Raw data downloaded from data sources, not manually modified.
    - `data/interim`: Intermediate data, pre-processed for further steps.
    - `data/processed`: Final processed data for modeling and analysis.
    - `data/external`: External datasets from other research teams for validation and comparison.

By default, the project does not track folders ending with `-private` and their contents, which can be used to store private files.

## Future Features

- Code tests
- Code format checks
- Continuous integration

## References

- Some useful coding principles: [Guiding Design Principles](https://nsls-ii.github.io/scientific-python-cookiecutter/guiding-design-principles.html#write-for-readability) (Many ideas in this project are inspired by these principles)
- Cookiecutter templates worth referencing:
    - [NSLS-II/scientific-python-cookiecutter](https://github.com/NSLS-II/scientific-python-cookiecutter)
    - [jbusecke/cookiecutter-science-project](https://github.com/jbusecke/cookiecutter-science-project/tree/master)