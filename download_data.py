from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import subprocess
import os
import json
import kaggle


api = KaggleApi()

# download the dataset using the kaggle API
api.dataset_download_files('uciml/electric-power-consumption-data-set', path=".")

# open the ZIP file in read mode
with zipfile.ZipFile('electric-power-consumption-data-set.zip', 'r') as zip_ref:
    # extract all files to the current working directory
    zip_ref.extractall()
