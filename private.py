#para gerar uma chave publica

n = int(input())
e = int(input())
phi = int(input())

k = 1
pd = (phi*k + 1)
while (pd%e!=0):
    k+=1
    pd = (phi*k + 1)

d = pd/e
print(k)
print("chave privada:{}".format(d))