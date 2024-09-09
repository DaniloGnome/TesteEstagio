# Função para inverter uma string manualmente
def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):  # Itera de trás para frente
        string_invertida += string[i]
    return string_invertida

# Entrada do usuário (ou você pode definir uma string diretamente no código)
entrada = input("Digite uma string: ")

# Chama a função para inverter a string
resultado = inverter_string(entrada)

# Exibe a string invertida
print(f"String invertida: {resultado}")
