class RecipeBook:
    def __init__(self):
        self.recipes = []

    def addRecipe(self, recipe):
        self.recipes.append(recipe)

    def deleteRecipe(self, recipeToDelete):
        if 0 <= recipeToDelete < len(self.recipes):
            return self.recipes.pop(recipeToDelete).getName()
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
            self.coffee >= recipe.getAmtCoffee()
            and self.milk >= recipe.getAmtMilk()
            and self.sugar >= recipe.getAmtSugar()
            and self.chocolate >= recipe.getAmtChocolate()
        ):
            self.coffee -= recipe.getAmtCoffee()
            self.milk -= recipe.getAmtMilk()
            self.sugar -= recipe.getAmtSugar()
            self.chocolate -= recipe.getAmtChocolate()
            return True
        return False

    def __str__(self):
        return f"Coffee: {self.coffee}\nMilk: {self.milk}\nSugar: {self.sugar}\nChocolate: {self.chocolate}"

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

class CoffeeMaker:
    def __init__(self):
        self.recipeBook = RecipeBook()
        self.inventory = Inventory()

    def addRecipe(self, r):
        self.recipeBook.addRecipe(r)

    def deleteRecipe(self, recipeToDelete):
        return self.recipeBook.deleteRecipe(recipeToDelete)

    def editRecipe(self, recipeToEdit, r):
        return self.recipeBook.editRecipe(recipeToEdit, r)

    def addInventory(self, amtCoffee, amtMilk, amtSugar, amtChocolate):
        self.inventory.addCoffee(amtCoffee)
        self.inventory.addMilk(amtMilk)
        self.inventory.addSugar(amtSugar)
        self.inventory.addChocolate(amtChocolate)

    def checkInventory(self):
        return str(self.inventory)

    def makeCoffee(self, recipeToPurchase, amtPaid):
        recipes = self.recipeBook.getRecipes()
        change = 0

        if 0 <= recipeToPurchase < len(recipes):
            if recipes[recipeToPurchase] is None:
                change = amtPaid
                
            elif recipes[recipeToPurchase].getPrice() <= amtPaid:
                if self.inventory.useIngredients(recipes[recipeToPurchase]):
                    change = amtPaid - recipes[recipeToPurchase].getPrice()
                else:
                    change = amtPaid
            else:
                change = amtPaid

        return change


cm = CoffeeMaker()
recipe  = Recipe('Cafe_diferenciado', 8,  1, 0, 7, 0)
cm.addRecipe(recipe)

print(cm.checkInventory())