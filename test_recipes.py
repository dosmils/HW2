import pytest

from main import Ingredient
from main import Recipe

test_cases = [("Мука", 500, "г"), ("Мука", 100, "г"), ("Яблоко", 500, "г"), ("Мука", 500, "кг")]


@pytest.fixture
def ingredient():
    return Ingredient("Мука", 500, "г")


def test_class_Ingredient_init(ingredient):
    assert ingredient.name == "Мука"
    assert ingredient.quantity == 500.0
    assert ingredient.unit == "г"


def test_class_Ingredient_str():
    ingredient = Ingredient("Мука", 500, "г")
    assert ingredient.__str__() == f"{ingredient.name}: {ingredient.quantity} {ingredient.unit}"


def test_class_Ingredient_eq():
    ingredient1 = Ingredient(*test_cases[0])
    ingredient2 = Ingredient(*test_cases[1])
    ingredient3 = Ingredient(*test_cases[2])
    ingredient4 = Ingredient(*test_cases[3])
    assert ingredient1.__eq__(ingredient2)
    assert not ingredient1.__eq__(ingredient3)
    assert not ingredient1.__eq__(ingredient4)


@pytest.fixture
def recipe():
    recipe = Recipe("Шарлотка")
    recipe.add_ingredient(Ingredient("Яйцо", 100, "г"))
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    return recipe


def test_class_Recipe_init(recipe):
    assert recipe.title == "Шарлотка"
    assert recipe.ingredients == [Ingredient("Яйцо", 100, "г"), Ingredient("Мука", 500, "г")]


def test_add_ingredient(recipe):
    new_ingredient = Ingredient("Мука", 500, "г")
    recipe.add_ingredient(new_ingredient)
    assert recipe.ingredients[1].quantity == 1000.0


def test_class_Recipe_scale(recipe):
    new_recipe = recipe.scale(100)
    assert new_recipe != recipe
    assert new_recipe.ingredients[0].quantity == 10000.0
    assert new_recipe.ingredients[1].quantity == 100000.0
    with pytest.raises(ValueError):
        recipe.scale(-100)


def test_class_Recipe_len(recipe):
    assert recipe.__len__() == 2


@pytest.fixture
def shopping_list():


