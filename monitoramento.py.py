

#Criando codigo para medir temperatura de geladeiras de mercado
lista_problemas= []
for g in range (12):
    nome_geladeira = input("digite o nome da geladeira: ")
    temperatura = float(input("digite a temperatura da geladeira:"))
    if  temperatura < -5 or temperatura > 10:
        lista_problemas.append(nome_geladeira)
print("Geladeiras com alerta:", lista_problemas)

