import pytest

from main import Ingredient

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
