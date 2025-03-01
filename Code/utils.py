#Generated with assistance of ChatGPT and references from prior projects

import subprocess
import sys

#List of required packages
REQUIRED_PACKAGES = ["pandas"]

def install_missing_packages():
    """Check and install missing packages."""
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
        except ImportError:
            print(f"🔍 {package} not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#Run package installation before importing
install_missing_packages()

#Import the packages
import pandas as pd
import os

#Set data directory
DATA_DIR = os.path.abspath(os.path.join(os.getcwd(), "../../", "Data"))
DEFAULT_FILE = "mortgage_covenant_data.csv"
def load_data(filename=DEFAULT_FILE):
    """Loads a predefined CSV file from the Data directory."""
    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {filename} not found in {DATA_DIR}")
    return pd.read_csv(file_path, low_memory=False)

if __name__ == "__main__":
    print("✅ Utils script loaded successfully.")


