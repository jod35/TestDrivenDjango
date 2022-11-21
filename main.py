import time
import turtle

names = ['Zoe','Joshua','Jerry','Isaac']

colors =['red','orange','yellow','green','blue','purple','pink']

turtle.bgcolor('pink')

for name in names:
    time.sleep(2)
    turtle.title(f"Name - {name}")

for color in colors:
    time.sleep(1)
    turtle.bgcolor(color)


turtle.done()


for name in names:
  time.sleep(2)
  turtle.title(name)