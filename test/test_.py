import pytest
#from ..coffee_maker import CoffeeMaker, Recipe, RecipeBook, Inventory
from ..gold import CoffeeMaker, Recipe, RecipeBook, Inventory

class TestCoffeeMaker:
    def setup_method(self):
        self.coffee_maker = CoffeeMaker()

    def test_add_recipe(self):
        recipe = Recipe('Cafe_diferenciado', 8, 1, 0, 7, 0)
        assert self.coffee_maker.addRecipe(recipe) in (None, True)

    def test_delete_recipe(self):
        recipe = Recipe('Cafe_diferenciado', 8, 1, 0, 7, 0)
        self.coffee_maker.addRecipe(recipe)
        assert self.coffee_maker.deleteRecipe(0) == 'Cafe_diferenciado'

    def test_edit_recipe(self):
        recipe = Recipe('Cafe_diferenciado', 8, 1, 0, 7, 0)
        recipe2 = Recipe('Cafezim', 8, 1, 0, 1, 0)
        self.coffee_maker.addRecipe(recipe)
        self.coffee_maker.addRecipe(recipe2)
        assert self.coffee_maker.editRecipe(0, recipe2) == 'Cafezim'

    def test_addInventory(self):
        qnt_cafe = 5
        qnt_leite = 5
        qnt_acucar = 6
        qnt_choco = 5
        assert self.coffee_maker.addInventory(qnt_cafe, qnt_leite, qnt_acucar, qnt_choco) is None

    def test_checkInventory(self):
        recipe = Recipe('Cafe_diferenciado', 8, 1, 0, 7, 0)
        self.coffee_maker.addRecipe(recipe)
        assert self.coffee_maker.checkInventory() == "Coffee: 15\nMilk: 15\nSugar: 15\nChocolate: 15"

    def test_buy_coffee(self):
        recipe = Recipe('Cafe_diferenciado', 8, 1, 0, 7, 0)
        recipe2 = Recipe('Cafe_diferenciadow', 1, 1, 0, 7, 0)
        self.coffee_maker.addRecipe(recipe)
        self.coffee_maker.addRecipe(recipe2)
        assert self.coffee_maker.makeCoffee(1, 8) == 7
