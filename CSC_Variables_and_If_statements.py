import random

x = 5
y = 50
if x==y or x<y:
  print("hi")
elif y/x==10:
  print("hello")
else:
  print("bye")


a = 10
b = 40
if a==b and a<b:
  print("yes")
elif a==b or a+b==50:
  print("no")
else:
  print("maybe")

cookies = 0

while cookies < 5:
  print("you still have cookies!")
  cookies = cookies + 1


for x in range(1, 5):
  print(x)


x=random.randrange(1, 10)
num = input("Guess Number: ")
if num==x:
  print("you are correct")
else:
  print("guess again")