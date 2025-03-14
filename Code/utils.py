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

#Merge the county datasets
DATA_DIR = os.path.abspath(os.path.join(os.getcwd(), "../../", "Data"))
HENNEPIN_FILE = os.path.join(DATA_DIR, "hennepin_covenant_data.csv")
RAMSEY_FILE = os.path.join(DATA_DIR, "ramsey_covenant_data.csv")
OUTPUT_FILE = os.path.join(DATA_DIR, "mortgage_covenant_data.csv")


#Merge the datasets
def merge_datasets():
    #Load the datasets
    hennepin_data = pd.read_csv(HENNEPIN_FILE)
    ramsey_data = pd.read_csv(RAMSEY_FILE)
    
    #Merge the datasets
    merged_data = pd.concat([hennepin_data, ramsey_data], ignore_index=True)
    
    #Save the merged dataset
    merged_data.to_csv(OUTPUT_FILE, index=False)

#Load the data
DEFAULT_FILE = "mortgage_covenant_data.csv"
def load_data(filename=DEFAULT_FILE):
    """Loads a predefined CSV file from the Data directory."""
    file_path = os.path.join(DATA_DIR, filename)
    merge_datasets()
    return pd.read_csv(file_path)
if __name__ == "__main__":
    print("✅ Utils script loaded successfully.")


