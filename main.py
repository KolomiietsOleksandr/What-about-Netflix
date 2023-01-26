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


def second_task():
    # First dataframe and see age categories
    dataframe = pandas.read_csv('titles.csv')
    age_categories = dataframe[dataframe['type'] == 'SHOW']

    # Second dataframe and set labels
    dataframe2 = age_categories.groupby('age_certification')['age_certification'].count()
    labels = set(age_categories[age_categories['age_certification'].notnull()]['age_certification'])

    plt.pie(dataframe2, labels=labels)

    plt.title('Age ratings')
    plt.show()


def third_task():

    dataframe = pandas.read_csv('titles.csv')

    # Sorting years
    films = dataframe[dataframe['release_year'] >= 2000]
     #years = list(films['release_year'].unique())
     #years.sort()
    films['above_8'] = films['imdb_score'] > 8.0
    films = films.groupby('release_year').mean()
    films['above_8'] = films['above_8'] * 100




    plt.plot( films.index, films['above_8'])
    plt.xlabel('year')
    plt.ylabel('percentage of movies and films')
    plt.show()

    most_successful_year = films['above_8'].idxmax()
    print(f'The most successful year is: {most_successful_year}')



first_task()
second_task()
third_task()












