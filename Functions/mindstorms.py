import turtle

def create_turtle(shapeType,shapeColor,speed):
    brad = turtle.Turtle()
    brad.shape(shapeType)
    brad.color(shapeColor)
    brad.speed(speed)

    return brad

def draw_square(shapeType,shapeColor,speed,length):
    
    brad = create_turtle(shapeType,shapeColor,speed)
   
    n = 0
    while n < 4:
        brad.forward(length)
        brad.left(90)
        n += 1
    

def draw_circle(shapeType,shapeColor,speed,radius):
    
    brad = create_turtle(shapeType,shapeColor,speed)

    brad.left(90)
    brad.circle(radius * 2)

def draw_Triangle(shapeType,shapeColor,speed,length):
    
    brad = create_turtle(shapeType,shapeColor,speed)
    
    n = 0
    while n < 3:
        brad.right(120)
        brad.forward(length)
        n += 1

def draw():
    window = turtle.Screen()
    window.bgcolor("yellow")
    draw_square("classic","red",1,100)
    draw_circle("circle","blue",1,50)
    draw_Triangle("arrow","green",1,100)

    window.exitonclick()

# draw()

def create_diamond(brad):
    
    brad.forward(50)

    brad.right(30)
    brad.forward(50)

    brad.right(150)
    brad.forward(50)

    brad.right(30)
    brad.forward(50)



def more_sheap():
    window = turtle.Screen()
    window.bgcolor("yellow")

    offset = 0
    add_offset = 360 / 36
    

    while offset < 360:
        brad = create_turtle("turtle","red",20)
        brad.right(offset)
        offset += add_offset
        create_diamond(brad)

    brad = create_turtle("turtle","red",20)
    brad.right(90)
    brad.forward(200)  

    window.exitonclick()

more_sheap()
# more_ling()