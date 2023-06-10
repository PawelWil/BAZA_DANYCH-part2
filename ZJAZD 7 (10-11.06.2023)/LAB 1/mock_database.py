from ingredient import Ingredient
from connection import connection


def add_ingredient(name, calories, protein, fat, carbs, fiber, ingredient_type) -> None:
    with connection.cursor() as cursor:
        cursor.execute("""
        INSERT INTO ingredients (ingredient_name, calories, protein, fat, carbs, fiber, ingredient_type)   
        VALUES  (?,?,?,?,?,?,?)
        """, (name, calories, protein, fat, carbs, fiber, ingredient_type))


def find_all():
    """
    Find all ingredients in list.
    :return: List of Ingredients
    """
    ingredients = []
    cursor = connection.cursor()
    for row in cursor.execute ("Select * from ingredients"):
        ingredients.append(Ingredient(*row))


def find_by_name_like(name: str):
    """
    Find all ingredients by name like
    :param name: name 'like'
    :return: list of ingredients
    """
    copy = find_all()
    result = []

    for ingredient in copy:
        if name.casefold() in ingredient.name.casefold():
            result.append(ingredient)

    return result
