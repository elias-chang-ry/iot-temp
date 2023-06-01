import os
import sys
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
sys.path.append("../src")
from data import preprocess_data
from features import build_features

def read_data(input_file_path):
    return pd.read_csv(input_file_path)

def process_data(dataframe):
    dataframe = preprocess_data.deduplicate(dataframe)
    dataframe = build_features.get_datetime_features(dataframe, 'noted_date')
    return dataframe_processed

def write_data(dataframe_processed, output_file_path):
    dataframe.to_csv(file_name, sep=',')

def check_write_data(dataframe, dataframe_processed):
    if dataframe.shape[1] > dataframe_processed.shape[1]:
        print('Duplicates has been removed')
    else:
        print('Duplicates has not been removed. Please check the dataset or modules used.')
        sys.exit(1)
    
    if dataframe.shape[0] > dataframe_processed.shape[0]:
        print('Features has been created.')
    else:
        print('Features has not been created. Please check the dataset or modules used.')
        sys.exit(1)

def main(input_file_path, output_file_path):
    try:
        dataframe = read_data(input_file_path)
    except IOError:
        print("Input file does not exist. Please try again")
        sys.exit(1)

    dataframe = process_data(dataframe)

    check_write_data(dataframe, dataframe_processed)

    write_data(dataframe, output_file_path)

main(input_file_path, output_file_path)