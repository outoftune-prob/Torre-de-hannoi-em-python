jogada = 1

def hanoi():
    def mova(n, origem, destino, aux):
        def mova_disco(de, para):
            global jogada
            print(f"Jogada {jogada:>3}: Tower {de} --> Tower {para}")
            jogada += 1

        if n == 1:
            mova_disco(origem, destino)
        else:
            mova(n - 1, origem, aux, destino)
            mova_disco(origem, destino)
            mova(n - 1, aux, destino, origem)

    n = int(input("Quantos discos deseja considerar? \n --> "))
    print(f"Solução do puzzle ({2 ** n - 1} jogadas):\n")
    mova(n, "1", "3", "2")


if __name__ == "__main__":
    hanoi()
