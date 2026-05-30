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

    def scale(self, ratio: float) -> Recipe:
        new_recipe = Recipe(self.title)
        for i in self.ingredients:
            new_ingredient = Ingredient(i.name, i.quantity * ratio, i.unit)
            new_recipe.ingredients.append(new_ingredient)
        return new_recipe

    def __len__(self) -> int:
        return len(self.ingredients)

    def __str__(self) -> str:
        return f"Название блюда: {self.title}. Ингредиенты: {'\n'.join(str(i) for i in self.ingredients)}."
