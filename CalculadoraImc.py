def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        imc = calcular_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")
        if imc < 18.5:
            print("Classificação: Abaixo do peso!")
        elif 18.5 <= imc < 25:
            print("Classificação: Peso normal")
        elif 25 <= imc < 30:
            print("Classificação: Sobrepeso")
        else:
            print("Classificação: Obesidade")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()