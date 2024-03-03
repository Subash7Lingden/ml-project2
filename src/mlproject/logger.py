import logging
import os
from datetime import datetime

LOG_FILE = "f{datetime.now(). strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE) ## generic code( folder name= logs, inside this LOG_FILE is created)
os.makedirs(log_path,exist_ok=True) # if folder is already availabe then we skip it.


LOG_FILE_PATH =os.path.join(log_path,LOG_FILE)## it is complete path of log which is the combination of LOG_FILE and log_path


## There is a format for setting  logging it and it has a function called basicConfig which tells where is log_file path and what is it's format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)