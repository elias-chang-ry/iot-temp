import pandas as pd

def deduplicate(dataframe):
    return dataframe.drop_duplicates(keep = 'last')

def sort_data(dataframe, sort_by):
    return dataframe.sort_values(by = [sort_by])