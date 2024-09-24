import lexico

#Arquivos de entrada e saida (já devem estar criados)
_in = open("_in.txt","r")
_out = open("_out.txt","w")

#Algoritimo principal
try:
    #Começa analise lexica
    lexico.start(_in,_out)
except Exception as e: 
    print("erro", str(e))