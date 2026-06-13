moyenne = float(input("Votre moyenne sur 20 au BAC: "))

if 12 <= moyenne < 14:
    print("Assez bien.")
elif 14 <= moyenne < 16:
    print("Bien.")
elif 16 <= moyenne < 18:
    print("Très bien.")
elif moyenne >= 18:
    print("Les félicitation du jury !")
else:
    print("Pas de mention")