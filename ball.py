from turtle import Turtle, xcor
class ball(Turtle):
    def __init__(self):
        super().__init__()  
        self.shape("circle")
        self.color("blue") 
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.x_move=10 
        self.y_move=10
        self.goto(x=0,y=0)
    def move(self):

        self.goto(x=self.xcor()+self.x_move,y=self.ycor()+self.y_move)  

    def bounce(self):
        self.y_move*=-1 
    def paddlehit(self):
        self.x_move*=-1  
    def reset(Self): 
        Self.goto(0,0)
        Self.y_move*=-1 
        Self.x_move*=-1 
    def stop(self):
        self.goto(x=0,y=0)


