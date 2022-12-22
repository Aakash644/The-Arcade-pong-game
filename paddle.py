from turtle import Turtle

class   paddle(Turtle):  
   def __init__(self,x,y):
       super().__init__() 
        
       self.shape("square") 
       self.color("white")  
       
       self.shapesize(stretch_wid=4,stretch_len=1) 
       self.penup() 
       self.goto(x=x,y=y)  


   def Up(self):
       self.goto(x=self.xcor(),y=self.ycor()+40)
   def Down(self):
       self.goto(x=self.xcor(),y=self.ycor()-40)