#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import*
G=6.673E-11
mass = {'earth': 5.97E24, 'moon': 7.36E22, 'sun':1.99E30}
radius = {'earth': 6.371E6*10, 'moon': 1.317E6*10, 'sun':6.95E8*10}
earth_orbit = {'r': 1.495E11, 'v': 2.9783E4}
moon_orbit = {'r': 3.84E8, 'v': 1.022E3}
theta = 5.145*pi/180.0

ratio = mass['moon']/(mass['moon']+mass['earth'])
count = 0
period = 0

def gforce(m1,m2,pos_vec):
    return -G*m1*m2/mag2(pos_vec)*norm(pos_vec)

scene = canvas(width = 800, height = 800, background = vec(0,0,0))
scene.lights = []
sun = sphere(pos = vec(0,0,0), radius = radius['sun'], color = color.orange, m = mass['sun'], v = vec(0,0,0), emissive = True)
local_light (pos = vec(0,0,0))

earth = sphere(pos = vec(earth_orbit['r']-moon_orbit['r']*ratio,0,0), radius = radius['earth'], m = mass['earth'], texture = {'file':textures.earth})
earth.v = vec(0,0,-(earth_orbit['v'] - ratio*moon_orbit['v']))

moon = sphere(pos = vec(earth_orbit['r'] + (1-ratio)*moon_orbit['r'], (1-ratio)*moon_orbit['r']*sin(theta),0), radius = radius['moon'], m = mass['moon'])
moon.v = vec(0,0, -(earth_orbit['v'] + (1-ratio)*moon_orbit['v']))

dt = 60*60
initial = cross(moon.pos - earth.pos, moon.v-earth.v)
a1 = arrow(color = color.white,)
a1.pos = earth.pos
a1.axix = 0.001*initial

t1=0
t2=0
t3=0

while (True):
    rate(1000)
    period += dt
    earth.a = (gforce(sun.m, earth.m, earth.pos - sun.pos) + gforce(moon.m, earth.m, earth.pos - moon.pos))/earth.m
    moon.a = (gforce(sun.m, moon.m, moon.pos - sun.pos) + gforce(earth.m, moon.m, moon.pos - earth.pos))/moon.m
    earth.v += earth.a*dt
    moon.v += moon.a*dt
    earth.pos += earth.v*dt
    moon.pos += moon.v*dt
    scene.center = earth.pos
    normvec = cross(moon.pos - earth.pos,moon.v - earth.v)
    a1.pos = earth.pos
    a1.axis = 0.001*normvec

    if  degrees(acos(dot(initial,normvec)/(mag(initial)*mag(normvec)))) < 0.1 and period/(60*60)> 10000 :
        print(period/(60*60*24*365),'years')
        break


# In[ ]:





# In[ ]:




