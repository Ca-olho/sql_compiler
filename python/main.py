import lexico
import sintatico

#Arquivos de entrada e saida (já devem estar criados)
_in = open("_in.txt","r")
_lex = open("_lex.txt","w")
_out = open("_out.txt","w")

#Lista de Tokens descobertos e posição
token_list = []
error_list = []

#Algoritimo principal
try:
    #Executa analise lexica
    lexico.start(_in,_lex,token_list,error_list)
    #Executa analise sintatica
    _lex = open("_lex.txt","r")
    sintatico.start(_lex,_out,token_list)

    #print(token_list)
    #print(error_list)
except Exception as e: 
    print("erro!", str(e))