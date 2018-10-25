avaliacoes = int(input('Há quantas avaliações?'))
notas = []
x = 0
while x < avaliacoes:
    notas.append(float(input('qual foi a sua nota?')))
    x+=1
soma=0
for y in range(0,avaliacoes):
    soma = notas[y] + soma
media = float(soma)/avaliacoes 
if media>=7:
    print('Parabens! aluno aprovado. Sua nota foi de:'+str(media)+'.')
elif 3<media<7:
    print('Aluno em recuperacao. Sua nota foi de:'+str(media)+'.')
else:
    print('aluno reprovado. Sua nota foi de:'+str(media)+'.')
    
    
