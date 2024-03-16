#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from vpython import*

amp=0.1
num=50
m=0.1
k=10
d=0.4

scene=graph(width=800,height=400,background=vec(0.7,0.3,0.5),range=4,fov=0.003,center=vec((num-1)*d/2,0,0))
p=gdots(color=color.cyan,graph=scene)

unitk=2*pi/(num*d)
for n in range(1,int(num/2-1)):
    wavevector=n*unitk
    phase=wavevector*np.arange(num)*d
    ball_pos,ball_v,spring_len=np.arange(num)*d+amp*np.sin(phase),np.zeros(num),np.ones(num)*d
    t,dt=0,0.0003
    
    while(ball_pos[1]-d>0):
        t+=dt
        spring_len[:-1]=ball_pos[1:]-ball_pos[:-1]
        spring_len[-1]=ball_pos[0]+num*d-ball_pos[-1]
        ball_v[1:]+=k*(spring_len[1:]-d)/m*dt-k*(spring_len[:-1]-d)/m*dt
        ball_v[0]+=k*(spring_len[0]-d)/m*dt-k*(spring_len[-1]-d)/m*dt
        ball_pos+=ball_v*dt
    p.plot(pos=(wavevector,2*pi/(t*4)))


# In[ ]:





# In[ ]:




