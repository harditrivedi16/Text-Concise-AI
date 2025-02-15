import os 
import sys 
import logging
'''
Defining the logging format: 
Ascii time: Save the timestamp where the code was executed
Label Name: Type of Log; eg: Info.
module: Which module(file: main.py etc) is being executed
Message: Message to be logged
'''
logging_str= "[%(asctime)s] %(levelname)s: %(module)s %(message)s"

#Creating Directory where the log files will be stored
log_dir= "logs"
log_filepath= os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
    
    level=logging.INFO,
    format=logging_str,

    handlers= [
        logging.FileHandler(log_filepath), #Print to log file
        logging.StreamHandler(sys.stdout)  # Print to console as well.
    ]
)

logger = logging.getLogger("textConciseLogger")
