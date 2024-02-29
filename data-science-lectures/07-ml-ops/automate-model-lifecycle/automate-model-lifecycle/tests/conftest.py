import pickle
import pandas as pd
import os
import pytest
import numpy as np

# from taxifare.params import DTYPES_RAW, DTYPES_PROCESSED

DTYPES_RAW = {
    "fare_amount": "float32",
    "pickup_datetime": "datetime64[ns, UTC]",
    "pickup_longitude": "float32",
    "pickup_latitude": "float32",
    "dropoff_longitude": "float32",
    "dropoff_latitude": "float32",
    "passenger_count": "int16"
}

DTYPES_PROCESSED = np.float32

@pytest.fixture(scope="session")
def fixture_query_1k()->pd.DataFrame:

    gcs_path = "https://storage.googleapis.com/datascience-mlops/taxi-fare-ny/solutions/data_query_fixture_2009-01-01_2015-01-01_1k.csv"
    df_raw = pd.read_csv(gcs_path, parse_dates=["pickup_datetime"])

    return df_raw


@pytest.fixture(scope='session')
def fixture_cleaned_1k()->pd.DataFrame:
    gcs_path = "https://storage.googleapis.com/datascience-mlops/taxi-fare-ny/solutions/data_cleaned_fixture_2009-01-01_2015-01-01_1k.csv"
    df_cleaned = pd.read_csv(gcs_path, parse_dates=["pickup_datetime"]).astype(DTYPES_RAW)

    return df_cleaned

@pytest.fixture(scope='session')
def fixture_processed_1k()->pd.DataFrame:
    gcs_path = "https://storage.googleapis.com/datascience-mlops/taxi-fare-ny/solutions/data_processed_fixture_2009-01-01_2015-01-01_1k.csv"
    df_processed = pd.read_csv(gcs_path, header=None, dtype=DTYPES_PROCESSED)

    return df_processed
