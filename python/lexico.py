#Estados
start_state = 0
error_state = 3
final_state = [1,2,3]

#Caracteres
separator = [' ',',',';','*','(',')','\'','$']

#Transições
#(estado atual, caracter atual da fita, proximo estado)
transition = [
    (0,'a',1),(0,'b',2),
    (1,'a',1),(1,'b',3),
    (2,'a',3),(2,'b',2),
    (3,'a',3),(3,'b',3)
]

#Procura o proximo estado
def next_state(state,char): #Estado e caracter da fita atuais
    #Percorre procurando uma regra de transição correspondente
    for t in transition:
        if t[0] == state and t[1] == char:
            #Retorna o proximo estado
            return t[2]
    return error_state

#Passa pelo arquivo de entrada verificando cada caracter
def start(_in,_out): #Acesso aos arquivos de input e output
    #Estado inicial
    state = start_state
    while 1:
        #Procura proxima caracter
        char = _in.read(1)
        #Se separador, salva e recomeça
        if char in separator:
            if state in final_state:
                _out.write(str(state))
            #Se ' ' não salva
            if char != ' ':
                _out.write(char)
            #Se final de sentença morre
            if char == '$':
                break
            state = start_state
            continue
        #Procura o proximo estado
        state = next_state(state,char)