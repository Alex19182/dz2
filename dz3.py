a=int(input("Введите 5-хзначное число: "))
n1 = a//10000
n2 = (a//1000)%10
n3 = (a//100)%10
n4 = (a//10)%10
n5 = a%10
b = (n5*10000)+(n4*1000)+(n3*100)+(n2*10)+n1
print(b)
input("press Enter for exit:")