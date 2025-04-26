# mdw_main/conftest.py
import sys
import os

# Add the 'mdw_main' directory to sys.path to make 'src' importable
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))




import logging
import pytest

from datetime import datetime

import os
from datetime import datetime

# Folder for log files
LOG_FOLDER = "logs"

# Create the log folder if it doesn't exist
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

# Generate a new log file for each test case and store it in the logs folder
@pytest.fixture(scope="session")
def logger(request):
    """Set up the logger for the tests with a unique log file for each test in the logs folder."""
    
    # Get the test name to use as part of the log filename
    test_name = request.node.name
    log_filename = os.path.join(LOG_FOLDER, f"{test_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
    
    # Create a custom logger
    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.INFO)
    
    # Create a file handler to write logs to a file in the 'logs' folder
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.INFO)
    
    # Create a console handler to output logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create a log formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Add formatter to both file and console handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    yield logger  # This will return the logger to the test
    
    # Cleanup after all tests are done (not necessary for logging)
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile

@pytest.fixture(scope="function")
def browser_fixture():
    # Créer un dossier temporaire unique pour chaque session de test
    temp_dir = tempfile.mkdtemp()

    # Configuration des options de Chrome
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument(f"--user-data-dir={temp_dir}")  # Dossier temporaire unique
    options.add_argument("--disable-extensions")  # Facultatif, mais utile pour éviter les extensions

    # Lancer le navigateur
    driver = webdriver.Chrome(options=options)

    # Assurer une fermeture propre
    yield driver
    driver.quit()
