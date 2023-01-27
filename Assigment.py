import pandas as pandas
import numpy as np
import matplotlib.pyplot as plt

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

    films['above_8'] = films['imdb_score'] > 8.0
    films = films.groupby('release_year').mean()
    films['above_8'] = films['above_8'] * 100

    plt.plot( films.index, films['above_8'])
    plt.xlabel('year')
    plt.ylabel('percentage of movies and films')
    plt.show()

    most_successful_year = films['above_8'].idxmax()
    print(f'The most successful year is: {most_successful_year}')


def forth_task():
    # Read Data
    dataframe = pandas.read_csv('titles.csv')
    actors = pandas.read_csv('credits.csv')
    # Find top 1000 films
    top1000 = dataframe[dataframe.type == 'MOVIE'].sort_values(by='imdb_score', ascending=False).iloc[:1000]
    # Find and sort actors by films number
    df = pandas.merge(top1000, actors, on="id")
    df2 = df.groupby(["person_id", "name"]).size().to_frame('Films Number')
    df3 = df2.reset_index("name").sort_values(by='Films Number', ascending=False).iloc[:10]
    df3.plot(kind="bar", x="name", rot=45, grid=True)
    plt.show()


first_task()
second_task()
third_task()
forth_task()











