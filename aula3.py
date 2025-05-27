usuarios = ["Arthur", "Beatriz", "Caio", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Júlia",
"Kauã", "Larissa", "Miguel", "Natália", "Otávio", "Olivia", "Pedro", "Patrícia", "Rafael", "Rafaela",
"Samuel", "Sabrina", "Thiago", "Tainá", "Victor", "Úrsula", "William", "Valentina", "André", "Yasmin",
"Bruno", "Zuleika", "Diego", "Clara", "Enzo", "Cecília", "Guilherme", "Elisa", "Heitor", "Lívia",
"Isaac", "Mariana", "Jorge", "Sofia", "Lucas", "Ana", "Benjamin", "Camila", "Daniel", "Eduarda",
"Felipe", "Gabriela", "Henrique", "Isabela", "João", "Karina", "Leonardo", "Luana", "Nicolas", "Maria",
"Alex", "Ariel", "Charlie", "Dani", "Dominique", "Emerson", "Francis", "Gabi", "Harley", "Indigo",
"Jaime", "Kai", "Logan", "Morgan", "Noel", "Orion", "Phoenix", "Quinn", "Riley", "Sam",
"Taylor", "Zion", "Avery", "Blair", "Casey", "Devon", "Eden", "Finley", "Gray", "Hunter",
"Jordan", "Kendall", "Leslie", "Milan", "Nico", "Ocean", "Robin", "Sky", "Terry", "Winter"]
contador = 0

for i in range(len(usuarios)):
    contador += 1
    divisao = contador % 15
   
    if divisao != 0 and (usuarios[i] != "Úrsula") and (usuarios[i] != "Devon"):
        print(usuarios[i])
       
    if (usuarios[i]) == "Úrsula":
        print(f"{usuarios[i]}, Bônus")
       
    if divisao == 0:
        print(f"{usuarios[i]}, teste")
   
    if i == 85:
        print(f"{usuarios[i]}, fim")
        break
