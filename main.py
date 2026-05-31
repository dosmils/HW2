class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title):
        self.title = title
        self.ingredients = []

    def add_ingredient(self, ingredient: Ingredient):
        for el in self.ingredients:
            if el == ingredient:
                el.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        return isinstance(ratio, (int, float)) and ratio > 0

    def scale(self, ratio: float):
        new_recipe = Recipe(self.title)
        for i in self.ingredients:
            new_ingredient = Ingredient(i.name, i.quantity * ratio, i.unit)
            new_recipe.ingredients.append(new_ingredient)
        return new_recipe

    def __len__(self) -> int:
        return len(self.ingredients)

    def __str__(self) -> str:
        return f"Название блюда: {self.title}. Ингредиенты: {'\n'.join(str(i) for i in self.ingredients)}."


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for i in scaled.ingredients:
            self._items.append((i, scaled.title))

    def remove_recipe(self, title: str):
        self._items = [el for el in self._items if el[1] != title]

    def get_list(self) -> list:
        shopping_list = {}
        answer = []
        for element in self._items:
            ingredient = element[0]
            if (ingredient.name, ingredient.unit) in shopping_list.keys():
                shopping_list[(ingredient.name, ingredient.unit)] += ingredient.quantity
            else:
                shopping_list[(ingredient.name, ingredient.unit)] = ingredient.quantity
        for i in shopping_list.keys():
            ingredient = Ingredient(i[0], shopping_list[(i[0], i[1])], i[1])
            answer.append(ingredient)
        answer.sort(key=lambda x: x.name)
        return answer

    def __add__(self, other):
        merged_shopping_list = ShoppingList()
        merged_shopping_list._items = self._items + other._items
        return merged_shopping_list


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title)
        self.diet_type = diet_type
        if ingredients:
            self.ingredients = ingredients


    def scale(self, ratio: float):
        scaled = super().scale(ratio)
        new_recipe = DietaryRecipe(self.title, self.diet_type)
        new_recipe.ingredients = scaled.ingredients
        return new_recipe

    def __str__(self):
        return f"Название блюда: [{self.diet_type}] {self.title}. Ингредиенты: {'\n'.join(str(i) for i in self.ingredients)}."




