import random

nomes = [
    "Adrian", "Angelo", "Arthur", "Carlos", "Christopher", "Douglas",
    "Emanuelly", "Everson", "Gabriel", "Guilherme", "Gustavo A.", "Gustavo D.",
    "Gustavo F.", "Isabella", "Jamile", "João M.", "João O.", "Joaquim",
    "Kalikey", "Luís", "Maria", "Pedro A.", "Pedro G.", "Rafael",
    "Raphael S.", "Raphael H.", "Roberto", "Sofia", "Stephanie"
]

nome_guilherme = "Guilherme"
nome_raphael_d = "Raphael S."

if nome_guilherme in nomes:
    nomes.remove(nome_guilherme)
if nome_raphael_d in nomes:
    nomes.remove(nome_raphael_d)

random.shuffle(nomes)

insert_pos = random.randint(0, len(nomes))
nomes.insert(insert_pos, nome_guilherme)
nomes.insert(insert_pos + 1, nome_raphael_d) # Insere Raphael S. logo depois de do meu nome

largura = max(len(nome) for nome in nomes) + 4

nomes_por_linha = 5

# Geração do Quadro

for i in range(0, len(nomes), nomes_por_linha):
    linha_atual_nomes = nomes[i : i + nomes_por_linha]

    linha_topo = "".join("+" + "-" * largura for _ in linha_atual_nomes) + "+"
    print(linha_topo)

    linha_meio = "".join("|" + nome.center(largura) for nome in linha_atual_nomes) + "|"
    print(linha_meio)

linha_base_final = "".join("+" + "-" * largura for _ in linha_atual_nomes) + "+"
print(linha_base_final)
