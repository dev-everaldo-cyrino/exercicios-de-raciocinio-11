tabela = []
tabela1 = []
total = 0
f = open('relatório.txt','w')
f.write('')
f.close()
while True:
    tabela.append(input('nome do usuario:  '))
    tabela1.append(float(input('espaço usado em MB: ')))
    op = input('adicionar mais (s/n): ')
    if op == 'n':
        break

#print('{},{}'.format(tabela,tabela1))
for x in range(len(tabela1)):
    total += tabela1[x]
#print(total)

f = open('relatório.txt','a')
f.write('------------------------------------------------------------------------ \n')
f.write('Espaço total ocupado: {} MB \n'.format(total))
f.write('Espaço médio ocupado: {:.2f} MB \n'.format(total/len(tabela1)))

arq1 = ['COGNITO Inc. Uso do espaço em disco pelos usuários','------------------------------------------------------------------------','Nr. Usuário       Espaço utilizado      %  do uso \n']
with open('relatório.txt','a')as arquivo:
    for x in arq1:
        arquivo.write(str(x)+'\n')
            
for x in range(len(tabela)):
    arq = ['{}  {}             {} MB               {:.2f} %'.format(x+1,tabela[x],tabela1[x],tabela1[x]/total)]
    with open('relatório.txt','a')as arquivo:
        for x in arq:
            arquivo.write(str(x)+'\n')
f.close()