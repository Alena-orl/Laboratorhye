numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
summ=0
lenght=len(numbers)

for i in range(lenght):
    if numbers[i]==None:
        numbers[i]=0
        k=i
    summ+=int(numbers[i])
numbers[k]=summ/(lenght)

print("Измененный список:", numbers)
