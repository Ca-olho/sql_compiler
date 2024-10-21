#Gramatica
    #S0 -> <S1>;
    #S1 -> C<A0>
    #S1 -> D<A0>
    #S1 -> S<B0>FV
    #S1 -> IOV(<C0>)L(<D0>)

    #A0 -> TV
    #A0 -> BV

    #B0 -> (<C0>)
    #B0 -> *

    #C0 -> V<C1>
    #C1 -> ,<C0>
    #C1 -> ε

    #D0 -> N<D1>
    #D0 -> 'V'<D1>
    #D1 -> ,<D0>
    #D1 -> ε

#Tamanho das produções
prod_size = [0,2,2,2,4,10,2,2,3,1,2,2,0,2,4,2,0]
prod_type = ['a','a','b',]
error_symbol = 'X'

#Tabela LR
start_state = 0
lr_table = [
    (0,'C','e',2),(0,'D','e',3),(0,'S','e',4),(0,'I','e',5),(0,'b','s',1),(1,';','e',6),(2,'T','e',8),(2,'B','e',9),(2,'c','s',7),(3,'T','e',8),
    (3,'B','e',9),(3,'c','s',10),(4,'(','e',12),(4,'*','e',13),(4,'d','s',11),(5,'O','e',14),(6,'$','a',-1),(7,';','r',1),(8,'V','e',15),(9,'V','e',16),
    (10,';','r',2),(11,'F','e',17),(12,'V','e',19),(12,'e','s',18),(13,'F','r',8),(14,'V','e',20),(15,';','r',5),(16,';','r',6),(17,'V','e',21),
    (18,')','e',22),(19,'(','r',11),(19,',','e',24),(19,'f','s',23),(20,'(','e',25),(21,';','r',3),(22,'F','r',7),(23,')','r',9),(24,'V','e',19),
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

#Procura o proximo estado
def next_state(state,char): #Estado e caracter da fita atuais
    #Percorre procurando uma regra de transição correspondente
    for t in transition:
        if t[0] == state and t[1] == char:
            #Retorna o proximo estado
            match t[2]:
                #Salta
                case 's':
                    #Empilha o proximo estado
                    stack.append(t[3])
                    return
                #Empilha
                case 'e':
                    #Empilha a caracter da fita e o proximo estado
                    stack.append(char)
                    stack.append(t[3])
                    return
                #Reduz
                case 'r':
                    #Reduz a quantidade de elementos equivalente ao tamanho da produção x 2
                    for i in range(2*prod_size[t[3]]):
                        stack.pop()
                    #Empilha o rotulo da produção
                    stack.append(prod_type[t[3]])
                    #Executa o mesmo algoritimo para achar o salto usando o topo da pilha (state) e o rotulo da produção que foi reduzida (char)
                    next_state(stack[-2],stack[-1])
                    return
                #Aceita
                case _:
                    #Empilha '$' para anunciar a aceitacao
                    stack.append(char)
                    return
    #Empilha 'X' para anunciar a rejeicao
    stack.append(error_symbol)
    return

def start(_in,_out): #Acesso aos arquivos de input e output
    return 0