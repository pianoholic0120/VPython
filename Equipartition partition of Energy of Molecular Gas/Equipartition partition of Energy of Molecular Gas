#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import*
import numpy as np
size, m_o, m_c, k_bond = 31E-12, 16.0/6E23, 12.0/6E23, 18600.0
d = 2.5*size
dt = 1E-16
class CO_molecule:
    def __init__(self, pos, axis):
        self.O = sphere(pos = pos, radius = size, color = color.red)
        self.C = sphere(pos = pos + axis, radius = size, color = color.blue)
        self.bond = cylinder(pos = pos, axis = axis, radius = size/2.0, color = color.white)
        self.O.m = m_o
        self.C.m = m_c
        self.O.v = vec(0,0,0)
        self.C.v = vec(0,0,0)
        self.bond.k = k_bond

    def bond_force_on_O(self):
        return self.bond.k*(mag(self.bond.axis)-d)*norm(self.bond.axis)

    def time_lapse(self, dt):   
        self.C.a = -self.bond_force_on_O() / self.C.m
        self.O.a = self.bond_force_on_O() / self.O.m
        self.C.v += self.C.a * dt
        self.O.v += self.O.a * dt
        self.C.pos += self.C.v * dt
        self.O.pos += self.O.v * dt
        self.bond.axis = self.C.pos - self.O.pos
        self.bond.pos = self.O.pos

    def com(self):
        return (self.O.m*self.O.pos + self.C.m*self.C.pos)/(self.C.m+self.O.m)
    def com_v(self):
        return (self.O.m*self.O.v + self.C.m*self.C.v)/(self.C.m + self.O.m)
    def v_P(self):
        return self.bond.k*(mag(self.bond.axis)-d)**2/2
    def v_K(self):
        C = self.C.m*(dot(self.C.v-self.com_v(),self.bond.axis)/mag(self.bond.axis))**2/2
        O = self.O.m*(dot(self.O.v-self.com_v(),self.bond.axis)/mag(self.bond.axis))**2/2
        return C+O
    def r_K(self):
        C = self.C.m*(mag(cross(self.C.v-self.com_v(),self.bond.axis))/mag(self.bond.axis))**2/2
        O = self.O.m*(mag(cross(self.O.v-self.com_v(),self.bond.axis))/mag(self.bond.axis))**2/2
        return C + O
    def com_K(self):
        return (self.C.m+self.O.m)*mag(self.com_v())**2/2
def collision(a1,a2):
     v1prime = a1.v - 2 * a2.m/(a1.m+a2.m) *(a1.pos-a2.pos) * dot (a1.v-a2.v, a1.pos-a2.pos) / mag(a1.pos-a2.pos)**2
     v2prime = a2.v - 2 * a1.m/(a1.m+a2.m) *(a2.pos-a1.pos) * dot (a2.v-a1.v, a2.pos-a1.pos) / mag(a2.pos-a1.pos)**2
     return v1prime, v2prime




N = 20 
L = ((24.4E-3/(6E23))*N)**(1/3.0)/50 
m = 14E-3/6E23 
k, T = 1.38E-23, 298.0 
initial_v = (3*k*T/m)**0.5
com_K = 0
v_P = 0
v_K = 0
r_K = 0

scene = canvas(width = 400, height =400, align = 'left', background = vec(1, 1, 1))
container = box(length = 2*L, height = 2*L, width = 2*L, opacity=0.4, color = color.yellow )
energies = graph(width = 600, align = 'left', ymin=0)
c_avg_com_K = gcurve(color = color.green)
c_avg_v_P = gcurve(color = color.red)
c_avg_v_K = gcurve(color = color.purple)
c_avg_r_K = gcurve(color = color.blue)

COs=[]

for i in range(N):
    O_pos = vec(random()-0.5, random()-0.5, random()-0.5)*L 
    CO = CO_molecule(pos=O_pos, axis = vector(1.0*d, 0, 0)) 
    CO.C.v = vector(initial_v*random(), initial_v*random(), initial_v*random()) 
    CO.O.v = vector(initial_v*random(), initial_v*random(), initial_v*random()) 
    COs.append(CO)

times = 0
dt = 5E-16
t = 0


while True:
    
    rate(3000)  
    for CO in COs:
        CO.time_lapse(dt)
        
    for i in range(N-1):
        for j in range(i+1,N):
            if mag(COs[i].C.pos-COs[j].C.pos)<=2*size and dot(COs[i].C.pos-COs[j].C.pos,COs[i].C.v-COs[j].C.v) <= 0:
                COs[i].C.v,COs[j].C.v = collision(COs[i].C,COs[j].C)
            if mag(COs[i].O.pos-COs[j].C.pos)<=2*size and dot(COs[i].O.pos-COs[j].C.pos,COs[i].O.v-COs[j].C.v) <= 0:
                COs[i].O.v,COs[j].C.v = collision(COs[i].O,COs[j].C)
            if mag(COs[i].C.pos-COs[j].O.pos)<=2*size and dot(COs[i].C.pos-COs[j].O.pos,COs[i].C.v-COs[j].O.v) <= 0:
                COs[i].C.v,COs[j].O.v = collision(COs[i].C,COs[j].O)
            if mag(COs[i].O.pos-COs[j].O.pos)<=2*size and dot(COs[i].O.pos-COs[j].O.pos,COs[i].O.v-COs[j].O.v) <= 0:
                COs[i].O.v,COs[j].O.v = collision(COs[i].O,COs[j].O)
                
    for CO in COs:#x y z
        if abs(CO.C.pos.x)>=L-size and CO.C.pos.x*CO.C.v.x>0:
            CO.C.v.x = -CO.C.v.x
        if abs(CO.C.pos.y)>=L-size and CO.C.pos.y*CO.C.v.y>0:
            CO.C.v.y = -CO.C.v.y
        if abs(CO.C.pos.z)>=L-size and CO.C.pos.z*CO.C.v.z>0:
            CO.C.v.z = -CO.C.v.z
        if abs(CO.O.pos.x)>=L-size and CO.O.pos.x*CO.O.v.x>0:
            CO.O.v.x = -CO.O.v.x
        if abs(CO.O.pos.y)>=L-size and CO.O.pos.y*CO.O.v.y>0:
            CO.O.v.y = -CO.O.v.y
        if abs(CO.O.pos.z)>=L-size and CO.O.pos.z*CO.O.v.z>0:
            CO.O.v.z = -CO.O.v.z
    for i in range(N):
        com_K += COs[i].com_K()
        v_K += COs[i].v_K()
        v_P += COs[i].v_P()
        r_K += COs[i].r_K()

    t += dt
    times += 1
    
    avg_com_K = com_K/times
    avg_v_K = v_K/times
    avg_v_P = v_P/times
    avg_r_K = r_K/times
    c_avg_com_K.plot(pos=(times,avg_com_K))
    c_avg_v_P.plot(pos=(times,avg_v_P))
    c_avg_v_K.plot(pos=(times,avg_v_K))
    c_avg_r_K.plot(pos=(times,avg_r_K))


# In[ ]:




