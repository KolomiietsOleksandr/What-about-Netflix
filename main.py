import matplotlib.pyplot as plt
import numpy as np
import pandas

def first_task():
    # Read data
    dataframe = pandas.read_csv('titles.csv')

    films = dataframe[dataframe['type'] == 'MOVIE']
    serials = dataframe[dataframe['type'] == 'SHOW']
    films_imdbs = list(films['imdb_score'])
    serials_imdbs = list(serials['imdb_score'])

    # Hist options and text
    names = ['Films IMDB', 'Serials IMDB']
    bins = np.arange(0, 10, 0.2)

    # Initialize hist
    plt.hist([films_imdbs, serials_imdbs], label=names, density=True, bins=bins, stacked=True)
    plt.legend()
    plt.title('IMDB')
    plt.xlabel('IMDB score')

    # Mean value
    print(f"Films mean value of IMDB is {round(films.loc[:, 'imdb_score'].mean(), 2)}")
    print(f"Serials mean value of IMDB is {round(serials.loc[:, 'imdb_score'].mean(), 2)}")

    plt.show()

first_task()
