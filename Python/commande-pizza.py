class Pizza:
    def __init__(self, base, prix, diametre, style, ingredients):
        self.base = base
        self.prix = prix
        self.diametre = diametre
        self.style = style
        self.ingredients = ingredients

    def ajouter_ingredients(self, nouvel_ingredient):
        if nouvel_ingredient == "ananas":
            raise TypeError("Les ananas ne vont pas sur les pizzas")
        self.ingredients.append(nouvel_ingredient)
        self.prix = self.prix + 1

    def servir(self, table):
        print("J'amène la pizza à la table", table)

    def livre(self, adresse):
        print("Je livre la pizza à l'adresse :", adresse)


base = input("Quelle base voulez-vous ? (tomate/crème) ")
taille = input("Quelle taille voulez-vous ? (moyenne/grande) ")
style = input("Quelle style voulez-vous ? (classique, calzone, stromboli ...) ")
ingredients = input("Quelle ingrédients voulez-vous ?")

diametre = 30
if taille == 'grande':
    diametre = 34

ingredients = ingredients.split(', ')

prix = 5 + len(ingredients)

pizza = Pizza(
    base=base,
    prix=prix,
    diametre=diametre,
    style=style,
    ingredients=ingredients
)

print(pizza.ingredients, pizza.prix)
pizza.ajouter_ingredients("olives")
print(pizza.ingredients, pizza.prix)
pizza.livre("9 rue du bois")
pizza.servir(13)
ananas = input("Voulez-vous ajouter des ananas ? (oui, non)")

if ananas == "oui":
    pizza.ajouter_ingredients("ananas")