import random

def m_of(n):
    subs = n
    n = n-1
    e = 0
    m = 0
    while True:
        if(n%2==0):
            e+=1
        else:
            m = n
            break
        n = int(n/2)
    #print("{} = {}".format(subs-1,(2**e)*m)) 
    #print("m={}e={}".format(m,e))
    return m  

#exponentiação modular
def mod_ex(x,y,p):#x^y mod p
    res = 1
    x = x % p #caso x seja maior que p
    #print(x,y,p,res)
    while(y>0):
        if(y&1): # Caso 'y' seja impar: y&1 retorna 1 (True)
            res = (res*x)%p
        y = y>>1 # é o mesmo que y/2
        x = (x*x)%p
        #print(x,y,p,res)
    return res

def miller_rabin(n, m):
    a = random.randint(2,n-2) 
    #um 'a' tal que 1 < a < n-1 ; (1 e n-1 NÃO INCLUSOS)
    #na funçao randint, 1 e n-1 seriam inclusos caso 'random.randint(1,n-1)'
    b = mod_ex(a,m,n)# b0 = a^m % n (I)
    
    #se b0 = -1 (b==1 or b==n-1)
    # pois o python não abarca resultados negativos no modulo
    if(b==1 or b==n-1):
        return True
    
    while (m != n-1):
        b = (b*b) % n #bi = b(i-1)^2 mod n
        m *=2 
        # ir multiplicando 'm' por potencias de 2 tal qual em (I) 
        # até m == n-1
        if(b==1):
            return False
        if(b==n-1):
            return True
    return False

def eh_primo(n):
    if(n==2 or n==3):
        return True
    if(n<=4):
        return False
    # numero 'm' tal que: n-1 = m*2^k 
    m = m_of(n)

    #grau de exatidão, já que é um teste probabilistico
    exato = 4 
    for i in range(exato):
        if(miller_rabin(n,m)==False):
            return False
    return True

n = int(input())
#print(m_of(n))

print(eh_primo(n))

