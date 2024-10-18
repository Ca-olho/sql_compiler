import lexico

#Arquivos de entrada e saida (já devem estar criados)
_in = open("_in.txt","r")
_lex = open("_lex.txt","r+")
_out = open("_out.txt","w")

#Lista de Tokens descobertos e posição
token_list = []

#Algoritimo principal
try:
    #Começa analise lexica
    lexico.start(_in,_lexout,token_list)
    
    #print(token_list)
except Exception as e: 
    print("erro", str(e))