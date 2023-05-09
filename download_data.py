from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import subprocess
import os

# create the .kaggle directory in the home directory
os.makedirs(os.path.expanduser('~/.kaggle'), exist_ok=True)

# copy the kaggle.json file to the .kaggle directory
shutil.copy('kaggle.json', os.path.expanduser('~/.kaggle/kaggle.json'))

# set the file permissions for the kaggle.json file
os.chmod(os.path.expanduser('~/.kaggle/kaggle.json'), 0o600)

os.environ['KAGGLE_USERNAME'] = "szk2001"
os.environ['KAGGLE_KEY'] = "9f337014bd79f6769bd9ba27c5774e49"

api = KaggleApi()
api.authenticate()

# download the dataset using the kaggle API
api.dataset_download_files('uciml/electric-power-consumption-data-set', path=".")

# open the ZIP file in read mode
with zipfile.ZipFile('electric-power-consumption-data-set.zip', 'r') as zip_ref:
    # extract all files to the current working directory
    zip_ref.extractall()