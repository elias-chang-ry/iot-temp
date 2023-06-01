import pandas as pd
import datetime as dt

def get_datetime_features(df, date_column): 
    df[date_column] = pd.to_datetime(df[date_column])
    df['date'] = df[date_column].dt.date
    df['year'] = df[date_column].dt.year
    #df['year_month'] = df[date_column].dt.to_period('M')
    #df['month_day'] = df[date_column].apply(lambda x: x.strftime("%m-%d") if pd.notnull(x) else '')
    df['month'] = df[date_column].dt.month
    df['month_name'] = df[date_column].dt.month_name()
    df['day'] = df[date_column].dt.day
    df['week'] = df[date_column].dt.isocalendar().week.astype(int)
    df['day_of_week'] = df[date_column].dt.dayofweek + 1
    df['day_of_week_name'] = df[date_column].dt.day_name()
    df['is_weekend'] = (df['day_of_week'] // 5 != 1).astype(int)
    df['time'] = df[date_column].dt.time
    df['hour'] = df[date_column].dt.hour
    df['minute'] = df[date_column].dt.minute
    df['second'] = df[date_column].dt.second
