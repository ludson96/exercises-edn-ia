'''
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''

temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Unidade de destino (C, F ou K): ").upper()

def converter(temp, origem, destino):
    if origem == destino:
        return temp
    # Convertendo origem para Celsius
    if origem == "F":
        temp = (temp - 32) * 5 / 9
    elif origem == "K":
        temp = temp - 273.15
    # Convertendo de Celsius para destino
    if destino == "F":
        return temp * 9 / 5 + 32
    elif destino == "K":
        return temp + 273.15
    else:
        return temp

resultado = converter(temperatura, origem, destino)
print(f"{temperatura}°{origem} = {resultado:.2f}°{destino}")
