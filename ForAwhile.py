Fruits = ["oranges","tamarind","banana"]
for x in Fruits:
    print(x)
for x in "tamarind":
    print(x)
for x in Fruits:
    print(x)
    if x == "tamarind":
        break
for x in "tamarind":
    print(x)
    if x == "i":
        break
for x in Fruits:
    if x == "tamarind":
        continue
    print(x)
for x in "tamarind":
    if x == "a":
        continue
    print(x)
i = 0
fruits = ("kiwi","coconut","apple")
while i < len(fruits):
    print(fruits[i])
    i+=1
for x in range(3):
    print(x)
for x in range(1,10):
    print(x)
for i in range(len(fruits)):
    print(fruits[i])
for fruit in fruits:
    for num in [1,2,3]:
        print(fruit, num)
Sum = 0
for num in range(1,21):
    if num % 2 == 0:
        Sum += num
print(Sum)


for number in range (1,10):
    for star in "*":
      star *= number
      print(star , end = " ")
    print()

for Number in range (1,6):
    for numbers in range (1,6):

       numbers *= Number
       print(numbers ,end = " ")
    print()

for NUMBER in range (1,11):
    for NUMBERS in [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
        NUMBER *= NUMBERS
        print(NUMBER ,end = " ")
    print()