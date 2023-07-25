def get_valid_year():
    # Função para obter um ano de nascimento válido entre 1922 e 2021.
    while True:
        try:
            # Solicita ao usuário o ano de nascimento e converte a entrada para um número inteiro.
            year = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            
            # Verifica se o ano de nascimento está dentro do intervalo permitido (1922 a 2021).
            if 1922 <= year <= 2021:
                return year
            else:
                print("Ano inválido. Digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

def calculate_age(year_of_birth):
    # Função para calcular a idade com base no ano de nascimento fornecido e o ano atual (2022).
    current_year = 2022
    age = current_year - year_of_birth
    return age

def main():
    # Função principal que executa o programa.
    print("Bem-vindo ao sistema de cálculo de idade!")
    
    # Solicita ao usuário o nome completo.
    name = input("Digite seu nome completo: ")
    
    # Chama a função para obter um ano de nascimento válido.
    year_of_birth = get_valid_year()
    
    # Calcula a idade com base no ano de nascimento fornecido e o ano atual (2022).
    age = calculate_age(year_of_birth)
    
    # Imprime uma mensagem de boas-vindas e a idade calculada.
    print(f"\nOlá, {name}!")
    print(f"No ano de 2022, você completou ou completará {age} anos de idade.")

if __name__ == "__main__":
    # Chama a função principal para iniciar o programa.
    main()