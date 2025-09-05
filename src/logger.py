import logging
import os
from datetime import datetime

# Create a "logs" folder in the current working directory
LOG_FOLDER = "logs"
logs_path = os.path.join(os.getcwd(), LOG_FOLDER)
os.makedirs(logs_path, exist_ok=True)

# Log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [%(lineno)d] [%(name)s] - %(levelname)s - %(message)s",
    level=logging.INFO,
)
