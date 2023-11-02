class InventoryException(Exception):
    pass


class Recipe:
    def __init__(self, name, price, amtCoffee, amtMilk, amtSugar, amtChocolate):
        self.name = name
        self.price = price
        self.amtCoffee = amtCoffee
        self.amtMilk = amtMilk
        self.amtSugar = amtSugar
        self.amtChocolate = amtChocolate

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getAmtCoffee(self):
        return self.amtCoffee

    def getAmtMilk(self):
        return self.amtMilk

    def getAmtSugar(self):
        return self.amtSugar

    def getAmtChocolate(self):
        return self.amtChocolate

class RecipeBook:
    def __init__(self):
        self.recipes = [None] * 4

    def addRecipe(self, recipe):
        for i in range(len(self.recipes)):
            if self.recipes[i] is None:
                self.recipes[i] = recipe
                return True
        return False

    def deleteRecipe(self, recipeToDelete):
        if 0 <= recipeToDelete < len(self.recipes) and self.recipes[recipeToDelete] is not None:
            name = self.recipes[recipeToDelete].name
            self.recipes[recipeToDelete] = None
            return name
        return None

    def editRecipe(self, recipeToEdit, newRecipe):
        if 0 <= recipeToEdit < len(self.recipes) and self.recipes[recipeToEdit] is not None:
            self.recipes[recipeToEdit] = newRecipe
            return newRecipe.name
        return None

    def getRecipes(self):
        return self.recipes


class Inventory:
    def __init__(self):
        self.coffee = 15
        self.milk = 15
        self.sugar = 15
        self.chocolate = 15

    def addCoffee(self, amtCoffee):
        self.coffee += int(amtCoffee)

    def addMilk(self, amtMilk):
        self.milk += int(amtMilk)

    def addSugar(self, amtSugar):
        self.sugar += int(amtSugar)

    def addChocolate(self, amtChocolate):
        self.chocolate += int(amtChocolate)

    def useIngredients(self, recipe):
        if (
            self.coffee >= recipe.amtCoffee
            and self.milk >= recipe.amtMilk
            and self.sugar >= recipe.amtSugar
            and self.chocolate >= recipe.amtChocolate
        ):
            self.coffee -= recipe.amtCoffee
            self.milk -= recipe.amtMilk
            self.sugar -= recipe.amtSugar
            self.chocolate -= recipe.amtChocolate
            return True
        return False

    def __str__(self):
        return f"Coffee: {self.coffee}\nMilk: {self.milk}\nSugar: {self.sugar}\nChocolate: {self.chocolate}"


class CoffeeMaker:
    def __init__(self):
        self.recipeBook = RecipeBook()
        self.inventory = Inventory()

    def addRecipe(self, recipe):
        return self.recipeBook.addRecipe(recipe)

    def deleteRecipe(self, recipeToDelete):
        return self.recipeBook.deleteRecipe(recipeToDelete)

    def editRecipe(self, recipeToEdit, newRecipe):
        return self.recipeBook.editRecipe(recipeToEdit, newRecipe)

    def addInventory(self, amtCoffee, amtMilk, amtSugar, amtChocolate):
        self.inventory.addCoffee(amtCoffee)
        self.inventory.addMilk(amtMilk)
        self.inventory.addSugar(amtSugar)
        self.inventory.addChocolate(amtChocolate)

    def checkInventory(self):
        return str(self.inventory)

    def makeCoffee(self, recipeToPurchase, amtPaid):
        change = 0

        recipes = self.recipeBook.getRecipes()
        if (
            recipeToPurchase < 0
            or recipeToPurchase >= len(recipes)
            or recipes[recipeToPurchase] is None
        ):
            change = amtPaid
        elif recipes[recipeToPurchase].price <= amtPaid:
            if self.inventory.useIngredients(recipes[recipeToPurchase]):
                change = amtPaid - recipes[recipeToPurchase].price
            else:
                change = amtPaid
        else:
            change = amtPaid

        return change

    def getRecipes(self):
        return self.recipeBook.getRecipes()
