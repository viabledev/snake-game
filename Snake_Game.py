#Snake game
from turtle import Turtle, Screen
import time
import random


Screen().setup(height=600, width=600)
Screen().bgcolor('black')
Screen().title('My Snake Game')
Screen().tracer(0)


#GLOBAL CONSTANTS
X_CORDINATE  = 10
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:

        def __init__(self): 
            self.segments = []
            self.create_snake()
            self.head = self.segments[0]


        def create_snake(self):
            global X_CORDINATE
            for x in range(0, 3):
                self.add_segment(X_CORDINATE)
        
        def add_segment(self, position):
                global X_CORDINATE
                tim = Turtle(shape='square')
                tim.penup()
                tim.goto(x=X_CORDINATE, y=0)
                tim.color('white')  
                X_CORDINATE -= 20
                self.segments.append(tim)

        def extend(self):
            self.add_segment(self.segments[-1].position())


        def move(self):

            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(x= new_x, y= new_y)
        
            self.head.forward(MOVE_DISTANCE)
        
        def up(self):
            if self.head.heading() != DOWN:
                self.head.setheading(UP)
        
        def down(self):
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

        def left(self):
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)



#CLASS INHERITENCE
class Food(Turtle):  #Turtle = Super class


        def __init__(self):
            super().__init__() #Importing everything from super class
            
            self.shape('circle')
            self.penup()
            self.shapesize(stretch_len=0.3, stretch_wid=0.3)
            self.color('red')
            self.speed('fastest')
            self.refresh()


        def refresh(self):
            x_random = random.randint(-280, 280)
            y_random = random.randint(-280, 280)
            self.goto(x=x_random, y=y_random)



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.write(f"Score Board: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
    
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score Board: {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER!", align="center", font=(18))





snake = Snake()
food = Food()
score = Score()

Screen().listen()
Screen().onkey(key='Up', fun=snake.up)
Screen().onkey(key='Down', fun=snake.down)
Screen().onkey(key='Left', fun=snake.left)
Screen().onkey(key='Right', fun=snake.right)



run = True

while run:
    
    Screen().update()
    time.sleep(0.1)
      
    snake.move()

    #Detect collison food
    if snake.head.distance(food) < 15:
        snake.extend()
        score.increase_score()
        food.refresh()
    
    #Detect collision wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        run = False
        score.game_over()
    
    #Detect collision tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            run = False
            score.game_over()




Screen().exitonclick()