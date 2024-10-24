#Gramatica
    #s0 -> s1 ;
    #s1 -> C a0
    #s1 -> D a0
    #s1 -> S b0 F V
    #s1 -> I O V ( c0 ) L ( d0 )

    #a0 -> T V
    #a0 -> B V

    #b0 -> ( c0 )
    #b0 -> *

    #c0 -> V c1
    #c1 -> , c0
    #c1 -> ''

    #d0 -> N d1
    #d0 -> ' V ' d1
    #d1 -> , d0
    #d1 -> ''

#Producoes
prod_size = [2,2,2,4,10,2,2,3,1,2,2,0,2,4,2,0]
prod_type = ['a','b','b','b','b','c','c','d','d','e','f','f','g','g','h','h']
error_symbol = 'X'

#Tabela LR
start_state = 0
error_state = -1
lr_table = [
    (0,'C','e',2),(0,'D','e',3),(0,'S','e',4),(0,'I','e',5),(0,'b','s',1),(1,';','e',6),(2,'T','e',8),(2,'B','e',9),(2,'c','s',7),(3,'T','e',8),
    (3,'B','e',9),(3,'c','s',10),(4,'(','e',12),(4,'*','e',13),(4,'d','s',11),(5,'O','e',14),(6,'$','a',-1),(7,';','r',1),(8,'V','e',15),(9,'V','e',16),
    (10,';','r',2),(11,'F','e',17),(12,'V','e',19),(12,'e','s',18),(13,'F','r',8),(14,'V','e',20),(15,';','r',5),(16,';','r',6),(17,'V','e',21),
    (18,')','e',22),(19,')','r',11),(19,',','e',24),(19,'f','s',23),(20,'(','e',25),(21,';','r',3),(22,'F','r',7),(23,')','r',9),(24,'V','e',19),
    (24,'e','s',26),(25,'V','e',19),(25,'e','s',27),(26,')','r',10),(27,')','e',28),(28,'L','e',29),(29,'(','e',30),(30,'N','e',32),(30,'\'','e',33),
    (30,'g','s',31),(31,')','e',34),(32,')','r',15),(32,',','e',36),(32,'h','s',35),(33,'V','e',37),(34,';','r',4),(35,')','r',12),(36,'N','e',32),
    (36,'\'','e',33),(36,'g','s',38),(37,'\'','e',39),(38,')','r',14),(39,')','r',15),(39,',','e',36),(39,'h','s',40),(40,')','r',13)
]
#(estado, caractere, acao)
    # e,N -> empilha e vai pra N
    # r,N -> reduz 2xTransicao N
    # s,N -> salto
    # a -> aceitacao

#Pilha
stack = []
stack.append(start_state)

#Executa a proxima ação sobre a pilha
def exec_lr_table(state,char): #Caracter atual da fita e estado no topo da pilha
    #Percorre procurando uma regra de transição correspondente
    for t in lr_table:
        if t[0] == state and t[1] == char:
            #Retorna o proximo estado
            match t[2]:
                #Salta
                case 's':
                    #Empilha o proximo estado
                    stack.append(t[3])
                    return 0
                #Empilha
                case 'e':
                    #Empilha a caracter da fita e o proximo estado
                    stack.append(char)
                    stack.append(t[3])
                    return 1
                #Reduz
                case 'r':
                    #Reduz a quantidade de elementos equivalente ao tamanho da produção x 2
                    for i in range(2*prod_size[t[3]]):
                        stack.pop()
                    #Empilha o rotulo da produção
                    stack.append(prod_type[t[3]])
                    #Executa o mesmo algoritimo para achar o salto usando o topo da pilha (state) e o rotulo da produção que foi reduzida (char)
                    exec_lr_table(stack[-2],stack[-1])
                    return 0
                #Aceita
                case _:
                    #Empilha '$' como simbolo de aceitacao
                    stack.append(char)
                    return 0
    #Empilha 'X' como simbolo de rejeicao
    stack.append(error_symbol)
    stack.append(error_state)
    return 1

def start(_in,_out): #Acesso aos arquivos de input e output
    #Variavel aux
    aux_ = 1
    while 1:
        #Procura proxima caracter
        if aux_ == 1:
            char = _in.read(1)
            aux_ = 0
        #Escreve no arquivo de saida o topo da pilha + a caracter atual da fita
        _out.write(str(stack[-1]) + ',' + char + '\n')
        #Executa a tabela, retorna 1 se empilhar a caractere da fita
        aux_ = exec_lr_table(stack[-1],char)
        #Se o topo da pilha for '$' aceita a cadeia e encerra
        if stack[-1] == '$':
            print('Aceita')
            _out.write('Acc')
            break
        #Se caracter da fita é final de sentença '$' e topo da pilha é erro 'X' encerra
        if stack[-2] == 'X' and char == '$':
            print('Rejeita')
            _out.write('Rej')
            break