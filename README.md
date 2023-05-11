# Consumption Pipeline

This repository contains a consumption pipeline for forecasting electrical power consumption using a Long Short-Term Memory (LSTM) neural network and an AutoRegressive Integrated Moving Average (ARIMA) model. The pipeline is designed to download and preprocess the data, train and evaluate the models, and upload the results to Firebase.

## Files and Folders

- `pipeline.yml`: A YAML file that defines the GitHub Actions workflow to automate the pipeline.
- `train_evaluate.py`: Python script that handles data preprocessing, model training and evaluation, and forecasting using the LSTM and ARIMA models.
- `firebase_upload.py`: Python script that uploads the prediction results to Firebase Realtime Database.
- `requirements.txt`: Lists the required Python packages to run the pipeline.

## Pipeline Workflow

1. Download the dataset from Kaggle using the Kaggle API.
2. Pre-process the data, handling missing values and resampling it to hourly frequency.
3. Normalize the data and split it into train and test sets.
4. Build and train the LSTM model, and evaluate its performance.
5. Forecast global active power using the ARIMA model.
6. Upload the forecast results to Firebase Realtime Database.

## Dependencies

- Python 3.8
- TensorFlow 2.12.0
- NumPy
- pandas
- Kaggle
- scikit-learn 1.2.2
- matplotlib 3.7.1
- seaborn 0.12.2
- requests
- firebase-admin
- statsmodels 0.14.0

## Usage

To run the pipeline, execute the following steps:

1. Clone the repository.
2. Set up the required environment variables:
   - `KAGGLE_USERNAME`: Your Kaggle username.
   - `KAGGLE_KEY`: Your Kaggle API key.
   - `FORECAST_KEY`: Your Firebase service account key (in JSON format).
3. Install the required Python packages using the `requirements.txt` file.
4. Run the `train_evaluate.py` script to train and evaluate the LSTM and ARIMA models.
5. Run the `firebase_upload.py` script to upload the forecast results to Firebase Realtime Database.

## License

This project is licensed under the MIT License.
