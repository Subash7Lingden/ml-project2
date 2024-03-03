import os # it givws generic folder path (not specific folder path)
from pathlib import Path # it creates the specific path
import logging


logging.basicConfig(level=logging.INFO)## generic inforation about logging deatils


project_name = "mlproject"

list_of_file=[
    ".github/workflows/.gitkeep",## use for deployment
    f"src/{project_name}/__init__.py", ## for making generic we use{projec_name}
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transfirmation.py",
    f"src/{project_name}/components/model_tranaier.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipelin.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt"
]

## logic
for filepath in list_of_file:
    filepath = Path(filepath) ## Path variable brings project relative path
    filedir, filename = os.path.split(filepath) # on splitiing we get two information filedir,file name


    if filedir !="":## if filedir not empty makedir, we also put logging.info on that dir
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):##if  path doesnot exist and and file size is zero. At this time we will open file, we also put logging.info on that file
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else: ## requirements.txt adn setup.py already exist it will skip that file and logging info tells us that file already exist
        logging.info(f"{filename} is already exists")
