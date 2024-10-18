import lexico
import sintatico

#Arquivos de entrada e saida (já devem estar criados)
_in = open("_in.txt","r")
_lex = open("_lex.txt","w")
_out = open("_out.txt","w")

#Lista de Tokens descobertos e posição
token_list = []

#Algoritimo principal
try:
    #Começa analise lexica
    lexico.start(_in,_lex,token_list)
    _lex = open("_lex.txt","r")
    sintatico.start(_lex,_out)
    #print(token_list)
except Exception as e: 
    print("erro", str(e))