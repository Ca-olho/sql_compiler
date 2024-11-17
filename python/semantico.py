import itertools

def start(_in,_out,list_t,list_e): #Acesso as listas e arquivos
    #Verifica se é Insert
    if list_t[0][3] == 'I':
        #Separa as variaveis do 'insert' da lista de tokens
        list_v = []
        last_num = list_t[0][0]
        for t in list_t:
            if t[3] == 'V' and t[0] == last_num+2:
                list_v.append(t)
                last_num = t[0]
        del list_v[0]
    else:
        return 0
    #Verifica se o nome das variaveis são todos distintos
    for v,w in itertools.combinations(list_v, 2):
        #Se não for adiciona a lista de erros e printa
        if v[2] == w[2]:
            list_e.append((w[0], w[1], w[2], 'M'))
            _out.write(f'- Erro semantico! Linha:{w[1]}, Token:"{w[2]}"\n')
