print("---------------------------")
a = float(input( "Введите вещественное число: "))
n = int(input("Введите степень: "))
i = 0
result = 0
for i in range(n+1):
    result += a**i

print( f"Ответ {result}" ) 
print("---------------------------")


