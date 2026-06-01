import random
from time import sleep

def andar():
    print("\nVoce esta caminhando...\n")
    sleep(1)
    return random.randint(0, 1) == 1

print("=-" * 30)
print("POKEMON")
print("=-" * 30)

pokemon = [
    {"nome": "Pikachu", "hp": 35, "ataque": 55, "defesa": 40},
    {"nome": "Bulbasaur", "hp": 45, "ataque": 49, "defesa": 49},
    {"nome": "Dratini", "hp": 41, "ataque": 64, "defesa": 45},
    {"nome": "Snorlax", "hp": 160, "ataque": 110, "defesa": 65},
    {"nome": "Ralts", "hp": 28, "ataque": 25, "defesa": 25}
]

pokemon_prof_carvalho = [
    {"nome": "Bulbasaur", "hp": 45, "ataque": 49, "defesa": 49},
    {"nome": "Charmander", "hp": 39, "ataque": 52, "defesa": 43},
    {"nome": "Squirtle", "hp": 44, "ataque": 48, "defesa": 65}
]

print("Pokemons iniciais: ")
for pk in pokemon_prof_carvalho:
    print(pk["nome"])
    print()

while True:
    pokemon_inicial = input("Fale o nome do pokemon: ").title()
    print()

    meu_pokemon = None
    for i in pokemon_prof_carvalho:
        if i["nome"] == pokemon_inicial:
            meu_pokemon = i
            break

    if meu_pokemon:
        print(f"Voce escolheu {meu_pokemon['nome']}!")
        print(f"Status \n HP: {meu_pokemon['hp']},"
              f"\n Ataque: {meu_pokemon['ataque']},"
              f"\n Defesa: {meu_pokemon['defesa']}")
        sleep(2)
        break
    else:
        print("Pokemon nao encontrado na lista do Professor Carvalho! "
              "Escolha entre Bulbasaur, Charmander ou Squirtle.")

while meu_pokemon["hp"] > 0:
    if andar():
        inimigo = random.choice(pokemon)
        print(f"O {inimigo['nome']} apareceu!")
        print(f"{meu_pokemon['nome']}, eu escolho voce!")
        turno = 1

        while meu_pokemon["hp"] > 0 and inimigo["hp"] > 0:
            print(f"\n--- {turno}° TURNO ---")
            print(f" {meu_pokemon['nome']}, HP: {meu_pokemon['hp']}")
            print(f" {inimigo['nome']}, HP: {inimigo['hp']}")
            print("\nO que fazer?")
            print("1. Atacar")
            print("2. Fugir\n")

            try:
                escolha = int(input("Escolha: "))

                if escolha == 1:
                    dano = random.randint(10, meu_pokemon['ataque'])
                    inimigo['hp'] -= dano
                    print(f" O {meu_pokemon['nome']} causou {dano} de dano!")

                    if inimigo['hp'] <= 0:
                        print(f"\nO {inimigo['nome']} foi derrotado! Voce venceu!")
                        sleep(2)
                        break

                    dano_inimigo = random.randint(8, inimigo['ataque'])
                    meu_pokemon['hp'] -= dano_inimigo
                    print(f"O {inimigo['nome']} causou {dano_inimigo} de dano!")

                    if meu_pokemon['hp'] <= 0:
                        print(f"\nO {meu_pokemon['nome']} desmaiou... Voce perdeu!")
                        break

                elif escolha == 2:
                    print("\nVoce fugiu da batalha!")
                    break

                else:
                    print("Opcao invalida!")

                turno += 1
                sleep(1)

            except ValueError:
                print("Digite um numero!")

print("\n=== FIM DA JORNADA ===")