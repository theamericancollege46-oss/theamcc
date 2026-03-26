a = [10, 20, 30, 40, 50]
sum1 = 0
i = 0

for val in a:
    sum1 += val  
    i += 1        
avg = sum1 / i if i != 0 else 0
print("Sum:", sum1)
print("Average:", avg)
