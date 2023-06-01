import pandas as pd
import datetime as dt
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="ticks", color_codes=True)

def plot_histogram_custom_bins(dataframe, data, histogram_bins, x_label, y_label, title):
    plt = dataframe[data].hist(bins = histogram_bins)
    plt.set_xlabel(x_label)
    plt.set_ylabel(y_label)
    plt.set_title(title)
    
def plot_bar(dataframe, data, sort, x_label, y_label, title):
    data = dataframe[data].value_counts(sort = sort)
    plt = data.plot.bar(xlabel = x_label, ylabel = y_label
                                                     , title = title, rot = 0);
    for index, data in enumerate(data):
        plt.text(x = index, y = data + 1, s = f"{data}", ha = 'center', va = 'bottom', fontweight = 'bold')
        
def plot_bar_count_groupby(dataframe, x, y, group_by, y_label, title):
    data = dataframe.groupby([x, y])[group_by].count()
    plt = data.unstack().plot.bar(ylabel = y_label
                                                     , title = title, rot = 0);

    for index, data in enumerate(data):

        # half the index in order for value positon to aline with thier corresponding x value, since position is int,
        # value will round up
        # e.g. index = 2 => position = 1, index = 3 => position = 2
        position = index / 2

        # adjustment for each group by value
        adjustment = 0

        if index % 2 == 0:
            adjustment = -0.13
        elif index % 2 == 1:
            adjustment = -0.37

        plt.text(x = position + adjustment, y = data + 1, s = f"{data}", ha = 'center', va = 'bottom', fontweight = 'bold')

def plot_line_aggregate_temp(dataframe, groupby):
        data = dataframe.groupby(groupby).agg({'temp': ['min', 'max', 'mean']})
        plt = data.plot.line(ylabel = 'Temperature', title = 'Min, Max & Mean Temperature of each ' + groupby, rot = 0)
        plt.legend(['Min', 'Max', 'Mean'], title = 'Temperature');
        
def plot_line_first_last_temp(dataframe, groupby):
        data = dataframe.groupby(groupby).agg({'temp': ['first', 'last']})
        plt = data.plot.line(ylabel = 'Temperature', title = 'First & last Temperature of each ' + groupby, rot = 0)
        plt.legend(['First', 'Last'], title = 'Temperature');

def plot_line_temp_filter(dataframe, agg_or_first_last, filter_by, filter_by_value, groupby):
        filter_df = dataframe[(dataframe[filter_by] == filter_by_value)]
        if agg_or_first_last == 'agg':
            plot_line_aggregate_temp (filter_df, groupby)
            plt.title('Min, Max & Mean Temperature of each ' + groupby + ' during ' + str(filter_by_value))
        elif agg_or_first_last == 'first_last':
            plot_line_first_last_temp (filter_df, groupby)
            plt.title('First & Last Temperature of each ' + groupby + ' during ' + str(filter_by_value))
        else:
            print("Agrument agg_or_first_last only accept 'agg' OR 'first_last'")