def a_power_b(x,y):
 contador=1
 for i in range (0,y):
  contador=contador*x
 return contador  
x=int(input("Digite un numero"))
y=int(input("Digite un numero o muere"))

efe=a_power_b(x,y)
print(efe)
