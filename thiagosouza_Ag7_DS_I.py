tipo_imovel = input("O imovel do senhor é comercial, casa ou apartamento? ").lower()
consumo = float(input("Qual o consumo em mensal em metros cubicos? "))

if tipo_imovel == "comercial": 
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tipo_imovel =="apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")
elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")     
 