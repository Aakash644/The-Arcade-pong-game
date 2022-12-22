from turtle import Turtle as t
class score(t):
    def __init__(self,x,y,name) :
        super().__init__() 
        self.name=name
        self.pos_x=x
        self.pos_y=y
        self.score=0 
        self.color("white") 
        self.penup() 
        self.goto(x=self.pos_x,y=self.pos_y) 
        self.write(arg=f"{self.name}:{self.score}",font="Arial 25" ) 
        self.hideturtle() 
    def refresh(self):
        self.clear() 
        self.score+=1  
        self.color("white") 
        self.penup() 
        self.goto(x=self.pos_x,y=self.pos_y) 
        self.write(arg=f"{self.name}:{self.score}",font="Arial 25" ) 
        self.hideturtle()  
    def gameover(self):
        self.color("white")  
        self.penup()
        self.goto(x=-60,y=0)
        self.write(arg=f"  Game over! \n{self.name} Wins", font="Arial 25") 
        

        
