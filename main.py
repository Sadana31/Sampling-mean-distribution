import pandas as pd 
import csv
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

def find_mean():
    population_mean = statistics.mean(data)
    print("")
    print("Mean of the total reading time is: ", population_mean)

def sample_means(counter):
    random_means = []
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        random_means.append(value)

    samples_mean = statistics.mean(random_means)
    return samples_mean
    
def find_sample_mean(counter):
    values = []
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        values.append(value)

    samples_mean = statistics.mean(values)
    print("Mean of the samples collected is: ",samples_mean)
    print("")

def plot_graph(meanList):
    df = meanList
    fig = ff.create_distplot([df],["reading_time"],show_hist=False,show_rug=False)
    fig.update_layout(title_text="Graph of the mean of reading time of articles")
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = sample_means(30)
        mean_list.append(set_of_means)

    plot_graph(mean_list)
    find_mean()
    find_sample_mean(30)

setup()

