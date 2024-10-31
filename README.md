execução:
  cd python
  python -u main.py

exemplos de entrada em '_in.txt':

  create table nome_tabela;$
    saida:
      Acc

  select (var0,var1) from nome_tabela ;$
    saida:
      Acc

  insert into nome_tabela(var0,var1,'var2') values('abc',-2,9);$
    saida:
      - Erro! Linha:1, Token:"-2"
      - Erro! Linha:1, Token:"'"
  
  drop database teste $
    saida:
      - Erro! Linha:1, Token:"$"
