class Cineminha:
    def __init__(self, filas=5, colunas=10):
        self.filas = filas
        self.colunas = colunas
        self.assentos = [['O' for _ in range(colunas)] for _ in range(filas)]

    def exibir_assentos(self):
        print("\nMapa dos assentos:")
        print("  " + " ".join(str(i) for i in range(self.colunas)))
        for i, fila in enumerate(self.assentos):
            print(str(i) + " " + " ".join(fila))

    def reservar_assento(self, fila, coluna):
        if 0 <= fila < self.filas and 0 <= coluna < self.colunas:
            if self.assentos[fila][coluna] == 'O':
                self.assentos[fila][coluna] = 'X'
                print(f"Assento ({fila}, {coluna}) reservado com sucesso!")
            else:
                print("Este assento já está reservado!")
        else:
            print("Posição inválida! Escolha um assento dentro do limite.")

def main():
    cineminha = Cineminha()
    while True:
        cineminha.exibir_assentos()
        try:
            fila = int(input("Informe o número da fila: "))
            coluna = int(input("Informe o número da coluna: "))
            cineminha.reservar_assento(fila, coluna)
        except ValueError:
            print("Entrada inválida! Digite números válidos.")
        continuar = input("Deseja reservar outro assento? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()

