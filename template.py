'''
This file was the first part that automatically created the template of the project 
and made all the files that we will need while working on the project.
'''

#Importing important libraries
import os
from pathlib import Path
import logging

#Setting the logging configuration and logging format
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "textConciseAI"

#Files as per project structure: 
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/comfiguration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/triasl.ipynb"
]

for filepath in list_of_files: 
    filepath = Path(filepath) # Gives filepath in the format of the os terminal
    filedir, filename = os.path.split(filepath)#Splits filepath into directory name and filename

    # Creating directories if they don't exist.
    if filedir != "": 
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the given filepath: {filename}")

    # Creating files if they don't exist or it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating file: {filepath}")

    else: 
        logging.info(f"File: {filepath} already exists.")

