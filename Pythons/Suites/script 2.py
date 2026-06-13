import turtle

def carre(t, taille):
    for _ in range(4):
        t.forward(taille)
        t.right(90)

n = int(input("n = ? "))
t = turtle.Turtle()
t.speed(0)

taille = 30
x = 0
y = 0

total = 0  # compteur de carrés

# Dessin des carrés
for ligne in range(1, n+1):
    for col in range(ligne):
        t.penup()
        t.goto(x + col * taille, y)
        t.pendown()
        carre(t, taille)
        total += 1
    y -= taille  # descendre d'une ligne

# Écriture du total sous le schéma
t.penup()
t.goto(0, y - 40)  # un peu plus bas que le dernier carré
t.pendown()
t.write(f"Total de carrés : {total}", font=("Arial", 16, "normal"))

# Déplacer la tortue en dehors du texte
t.penup()
t.goto(200, -200)  # tu peux changer ces valeurs si tu veux
t.pendown()

turtle.done()
