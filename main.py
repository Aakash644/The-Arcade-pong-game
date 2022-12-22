from turtle import Turtle as t,Screen as s
import time 
from score import score
from ball import ball
from paddle import paddle 
#screen setup
screen=s() 
screen.setup(width=800,height=600) 
screen.bgcolor("black") 
screen.title("Pong Game")
screen.tracer(0) 
#creating left & right paddles
paddle_left=paddle(-360,40)
paddle_right=paddle(360,40) 
ballobj=ball()   
#score
playerA=score(-160,260,"PlayerA") 
playerB=score(40,260,"PlayerB")
screen.listen()  
#key methods
screen.onkey(key="w",fun=paddle_left.Up)
screen.onkey(key="s",fun=paddle_left.Down) 
screen.onkey(key="o",fun=paddle_right.Up)
screen.onkey(key="l",fun=paddle_right.Down) 
gameison=True  
while gameison: 
    time.sleep(0.05)
    screen.update()
    #movement of ball
    ballobj.move()  
    # detect collision with wall
    if(ballobj.ycor()>280 or ballobj.ycor()<-280):
        ballobj.bounce() 
    # detect collision with paddle
    if(paddle_left.distance(ballobj)<50 or paddle_right.distance(ballobj)<50): 
        if(ballobj.xcor()<320 or ballobj.xcor()>-320):
            ballobj.paddlehit() 
    # detect when paddle miss the ball and update the score
    if(ballobj.xcor()>380):
        playerA.refresh()
    elif(ballobj.xcor()<-380):
        playerB.refresh()  
    #detect gameover
    if (playerA.score>=10 ): 
        ballobj.stop()
        playerA.gameover()
    elif(playerB.score>=10): 
        ballobj.stop()
        playerB.gameover() 
    #service 
    if( ballobj.xcor()>380  or ballobj.xcor()<-380):
        ballobj.reset()
    

screen.exitonclick()