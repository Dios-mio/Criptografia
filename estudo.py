import random
from fractions import gcd
chamada=str(input("Digite uma valor: "))
string="abcdefghijklmnopqrstuvxyv0123456789*.&%$#@!?"
tupla={}
vetorReal=[]
alfa={}
teste=[]
resposta=[]
#converter os valores da cript nos valores reais da mensagem
def descript (privada,conjunto):
	p=''
	for key in range(0,len(teste)):
		##formulada equação e anexar valores em uma lista e depois adiciona-lo em uma string 
		m=teste[key]**privada%conjunto
		resposta.append(m)
		for y in alfa:
			if(y==resposta[key]):
				p+=alfa.get(y)
	print("Descriptografia: ",p)
##chave privada
def chavePrivada(chave,totti,conjunto):
	d=0
	##formula da chave privada
	while(mod(d*chave,totti)!=1):
		d+=1
	descript(d,conjunto)
	return d

##faz uma comparação do mdc para a<b, pois a formula tradiconal terá um problema com a divisão por zero
def mod(a,b):
	if(a<b):
		return a
	else:
		c=a%b
		return c 
		
##mdc e criação da chave pública 
def mdc(totiente,conjunto):
	caix=[]
	for chave in range(2,800):
		t=gcd(totiente,chave)
		if(t==1):
			caix.append(t)
			if(len(caix)==5):
				del caix
				break;	
	cript(conjunto,chave)
	#verificar se a chave é 13
	##chave=gcd(b,t)
	privd=chavePrivada(chave,totiente,conjunto)
	
##buscar um elemento primo aleatório
def buscar():	#gerar quarenta números aleatórios
	for i in range(1,40):	
		#entre os valores A e B		
		number2=random.randint(21,300)
		primo(number2)


	var=random.randint(0,2)
	var1=random.randint(0,2)
	##verifica se os valores de primo são diferentes
	while(var==var1):
		var1=random.randint(0,2)
		if(var1 !=var ):
			break
	
	#salva os valores primos
	primo1=vetorReal[var]
	primo2=vetorReal[var1]
	
	conjunto=primo1*primo2
	##equação da formula Euler co-primo
	totiente=(primo1-1)*(primo2-1)
	mdc(totiente,conjunto)
	del var
	del var1
	

#verificar se o valor é primo ou nao. Caso seja, adiciona o valor em um vetor
def primo(number2):
		vetor=[]
		for x in range(1,number2+1):
			if(number2 % x == 0):
				vetor.append(x)
#Uso um vetor para adicionar todos as divisões possíveis. Caso seja menor que dois o total de divisões, o número será primo.
				if(len(vetor)>2):
					vetor.clear()
					break
		if(len(vetor)==2):
			vetorReal.append(number2)

#separar e adicionar elementos de uma string associada a um número
def cript(conjunto,publico):
	cont=0
	p=''
	for f in(chamada):
		if(chamada[cont:cont+1]):
			for key in alfa:
				if(alfa.get(key)==chamada[cont:cont+1]):
					##equação da formula e jogando a criptografia de cada valor para uma variável tipo String
					c=(key**publico) % conjunto
					teste.append(c)
					p+=str(c)
			cont=cont+1
	print("criptografia: ",p)
	return p
#anexar valores fixos nao ASCII para cada valor do alfabeto
def associar():
	int=0
	val=random.randint(1,500)	
	for x in(string):
		if(string[int:int+1]):
			alfa[val]=string[int:int+1]
		int=int+1
		val=val+3

associar()
buscar()
##print("Valores do alfabeto: \n",alfa)


