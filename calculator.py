def calculator():
    print("Bienvenue dans la calculatrice simple!")
    while True:
        try:
            x = float(input("Entrez le premier nombre: "))
            op = input("Entrez l'opérateur (+, -, *, /) ou 'q' pour quitter: ")
            if op == 'q':
                print("Au revoir!")
                break
            y = float(input("Entrez le deuxième nombre: "))
            if op == '+':
                print(f"Résultat: {x + y}")
            elif op == '-':
                print(f"Résultat: {x - y}")
            elif op == '*':
                print(f"Résultat: {x * y}")
            elif op == '/':
                if y == 0:
                    print("Erreur: division par zéro!")
                else:
                    print(f"Résultat: {x / y}")
            else:
                print("Opérateur invalide!")
        except ValueError:
            print("Entrée invalide, veuillez entrer des nombres.")
            
if __name__ == "__main__":
    calculator()
