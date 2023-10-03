from scripts import PopulationModel

import requests


def download_population_data(url, filename):
    response = requests.get(url)
    response.raise_for_status()  # Check if request was successful
    with open(filename, 'wb') as file:
        file.write(response.content)


# Example usage:


if __name__ == '__main__':
    # Download historic population data
    # url = 'https://example.com/historic_population_data.csv'
    # filename = 'population_data.csv'
    # download_population_data(url, filename)

    population_model = PopulationModel(n_initial=1000, child_probability=0.12)
    population_model.evolve(500)
    population_model.plot()
    population_model.plot_children_per_person()
