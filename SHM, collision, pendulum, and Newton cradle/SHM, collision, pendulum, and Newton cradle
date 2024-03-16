from vpython import*
N = input('請輸入數字1-4:')
con_N = int(N)
L = 2 
k = 150000
size = 0.2 #ball radius
mass = 1.0 #ball mass 
scene = canvas(width = 800, height =800, center=vec(0, 0, 0), background=vec(0.5,0.5,0)) # open window
ceiling = box(length=2.0, height=0.005, width=0.8, color=color.blue)
dt = 0.0001
g = vec(0, -9.8, 0)
t=0
a=0
b=0
oscillation1 = graph(width = 450, align = 'left')
funct1 = gcurve(graph = oscillation1, color=color.red, width=4)#kinetic energy
funct2 = gcurve(graph = oscillation1, color=color.blue, width=4)#potential energy
oscillation2 = graph(width = 450, align = 'right')
funct3 = gcurve(graph = oscillation2, color=color.red, width=4)#kinetic energy
funct4 = gcurve(graph = oscillation2, color=color.blue, width=4)#potential energy

balls = []
for i in range(5):
    if (i<con_N):
        ball = sphere(pos = vec((i-2)*0.4-0.44441, -L+0.05, 0), radius = size, color=color.red)
    if (i>=con_N):
        ball = sphere(pos = vec((i-2)*0.4, -L, 0), radius = size, color=color.red)
    ball.v = vec(0, 0, 0)
    balls.append(ball)

springs =[]
for i in range(5):
    spring = helix(radius=0.02, thickness =0.01)
    spring.pos = vec((i-2)*0.4, 0, 0)
    spring.axis = balls[i].pos-spring.pos
    springs.append(spring)
    
spring_forces =[]

sum_of_k = 0
sum_of_g = 0

while True:
    rate(5000)
    t += dt    
    a = 0
    b = 0
    for i in range(5):
        springs[i].axis = balls[i].pos - springs[i].pos #spring extended from endpoint to ball
        spring_forces = - k * (mag(springs[i].axis) - L) * springs[i].axis.norm() # to get spring force vector
        balls[i].a = g + spring_forces / mass # ball acceleration = - g in y + spring force /m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
        a+=(1/2)*(mag(balls[i].v))*(mag(balls[i].v))         
        b+=9.8*(balls[i].pos.y+L)
    
    funct1.plot(pos=(t,a))
    funct2.plot(pos=(t,b))
    sum_of_k += a
    sum_of_g += b
    funct3.plot(pos=(t,sum_of_k/t))
    funct4.plot(pos=(t,sum_of_g/t))

    for i in range(4):
        if mag(balls[i].pos-balls[i+1].pos)<=0.4:
            if balls[i].v.x >= 0 and balls[i+1].v.x <= 0:
                tmp = balls[i].v
                balls[i].v = balls[i+1].v
                balls[i+1].v = tmp
                            
