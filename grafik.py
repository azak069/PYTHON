import turtle as t

p = t.Turtle()
p.speed(0)
t.bgcolor("black")
warna = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(360):
    p.color(warna[i % 6])
    p.forward(i * 2)
    p.left(55)

p.hideturtle()
t.done()

# Program ini mendemonstrasikan penggunaan modul turtle untuk menggambar pola warna-warni di Python.