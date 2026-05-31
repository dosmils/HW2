import pytest

from main import Ingredient
from main import Recipe
from main import ShoppingList

test_cases = [("Мука", 500, "г"), ("Мука", 100, "г"), ("Яблоко", 500, "г"), ("Мука", 500, "кг")]
test_cases_shopping_lists = []


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
    shopping_list = ShoppingList()
    recipe = Recipe("Шарлотка")
    recipe.add_ingredient(Ingredient("Яйцо", 100, "г"))
    recipe_1 = Recipe("Шарлотка")
    recipe_1.add_ingredient(Ingredient("Мука", 100, "г"))
    shopping_list.add_recipe(recipe, 100)
    shopping_list.add_recipe(recipe_1, 100)
    return shopping_list


@pytest.fixture
def shopping_list1():
    shopping_list1 = ShoppingList()
    recipe = Recipe("Салат")
    recipe.add_ingredient(Ingredient("Яйцо", 10, "г"))
    shopping_list1.add_recipe(recipe, 100)
    return shopping_list1


@pytest.fixture
def shopping_list2():
    shopping_list2 = ShoppingList()
    recipe = Recipe("Шарлотка")
    recipe.add_ingredient(Ingredient("Яйцо", 100, "г"))
    recipe_1 = Recipe("Шарлотка")
    recipe_1.add_ingredient(Ingredient("Мука", 100, "г"))
    shopping_list2.add_recipe(recipe, 100)
    shopping_list2.add_recipe(recipe_1, 100)
    return shopping_list2


def test_class_ShoppingList_add_recipe(shopping_list, recipe):
    right_recipe = recipe
    shopping_list.add_recipe(right_recipe, 10)
    assert len(shopping_list._items) > 0
    wrong_recipe = Recipe("Салат")
    with pytest.raises(ValueError):
        shopping_list.add_recipe(wrong_recipe, -100)


def test_class_ShoppingList_remove_recipe(shopping_list, recipe):
    shopping_list.remove_recipe("Шарлотка")
    assert all(el[1] != "Шарлотка" for el in shopping_list._items)
    shopping_list.remove_recipe("Салат")
    assert all(el[1] != "Салат" for el in shopping_list._items)


def test_class_ShoppingList_get_list(shopping_list):
    result = shopping_list.get_list()
    egg = next(i for i in result if i.name == "Яйцо")
    assert egg.quantity == 10000.0
    names = [i.name for i in shopping_list.get_list()]
    assert names == sorted(names)


def test_class_ShoppingList_add(shopping_list1, shopping_list2):
    shop_list1_copy, shop_list2_copy = shopping_list1._items.copy(), shopping_list2._items.copy()
    new_shopping_list = shopping_list1.__add__(shopping_list2)
    assert new_shopping_list
    assert shop_list1_copy == shopping_list1._items
    assert shop_list2_copy == shopping_list2._items
