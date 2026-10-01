list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list :
    if num % 2 == 0 :
     print (num)
     
def celsius_to_farenhiet(celsius):
  farenhiet = (celsius * 9/5)+32
  return (farenhiet)
print(celsius_to_farenhiet(25))