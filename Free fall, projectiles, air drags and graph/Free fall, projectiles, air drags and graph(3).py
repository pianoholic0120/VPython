from vpython import *
g=9.8 
size=0.25
C_drag=0.9
theta=pi/4
n=0
height1=size
distance=0

scene=canvas(center = vec(0,5,0), width=600, background=vec(0.5,0.5,0))
floor=box(length=300, height=0.01, width=4, color=color.blue)
ball=sphere(radius = size, color=color.red, make_trail=True, trail_radius = size/3)
a1 = arrow(color = color.white, shaftwidth = 0.1)
oscillation = graph(width = 450, align = 'right')
funct1 = gdots(graph = oscillation, color=color.blue, size=3)
t=0

a1.pos=vec(-15.0,size,0)
a1.axis=vec(20*cos(theta), 20*sin(theta), 0)

ball.pos=vec(-15.0,size,0)
ball.v=vec(20*cos(theta), 20*sin(theta), 0)
dt=0.001

while ball.pos.x<300:
    if n==3: 
        break
    rate(1000)
    distance+=(dt*ball.v).mag
    ball.v += vec(0, -g, 0) * dt - C_drag*ball.v*dt
    ball.pos += ball.v*dt
#   vt graph
    funct1.plot(pos=(t, ball.v.mag))
    t = t + 1
#   
    a1.axis=ball.v+vec(0, -g, 0) * dt - C_drag*ball.v*dt
    a1.pos=ball.pos+ball.v*dt
    if height1<=ball.pos.y+ball.v.y*dt: 
        height1=ball.pos.y+ball.v.y*dt
    if ball.pos.y <= size and ball.v.y <0: 
        ball.v.y = - ball.v.y
        n+=1


print('the largest height=')
print(height1)
print('the displacement of the ball=')
print(ball.pos.x+15)
print('the distance of the ball=')
print(distance)
