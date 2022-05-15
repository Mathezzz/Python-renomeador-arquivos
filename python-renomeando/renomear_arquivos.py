import os

i = 1
pasta = './python-renomeando'
arquivos = os.listdir(pasta)
print(arquivos)
for arquivo in arquivos[1:]:
    nome_antigo = os.path.join(pasta, arquivo)
    nome_novo = os.path.join(pasta, 'arquivo_0' + str(i) + '.txt')
    os.rename(nome_antigo, nome_novo)
    i = i+1
arquivos = os.listdir(pasta)
print(arquivos)