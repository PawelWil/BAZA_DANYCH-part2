import csv
import database


def load_initial_data(filename='ingredients.csv') -> None:
    with open(filename, 'r', encoding='UTF-8', newline='') as ingredients_file:
        reader = csv.reader(ingredients_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        ingredients_file.readline()  # Ignore headers
        for row in reader:
            database.add_ingredient(*row)
