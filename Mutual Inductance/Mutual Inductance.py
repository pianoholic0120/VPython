#!/usr/bin/env python
# coding: utf-8

# In[1]:


import vpython as vp
import numpy as np

LL_i, LL_r, SL_i, SL_r,d=1, 0.12, 1, 0.06, 0.1
m=1000
S_m_area=np.array([((SL_r*i/m)**2-(SL_r*(i-1)/m)**2)*vp.pi for i in range(1,m+1)])
L_m_area=np.array([((LL_r*i/m)**2-(LL_r*(i-1)/m)**2)*vp.pi for i in range(1,m+1)])
n=1000
theta=np.array([2*vp.pi*i/n for i in range(n)])
L_ds=2*vp.pi*LL_r/n
L_dl=[vp.vec(-L_ds*vp.sin(theta[i]),L_ds*vp.cos(theta[i]),0) for i in range(n)]
L_pos=[vp.vec(vp.cos(theta[i])*LL_r,vp.sin(theta[i])*LL_r,0) for i in range(n)]

S_ds=2*vp.pi*SL_r/n
S_dl=[vp.vec(-S_ds*vp.sin(theta[i]),S_ds*vp.cos(theta[i]),0) for i in range(n)]
S_pos=[vp.vec(vp.cos(theta[i])*SL_r,vp.sin(theta[i])*SL_r,d) for i in range(n)]
mu0=4E-7*vp.pi

scene=vp.canvas(width=600,height=600,center=vp.vec(0,0,0.05),background=vp.color.yellow,forward=vp.vec(-1,0,0),up=vp.vec(0,0,1))
z_axis=vp.arrow(pos=vp.vec(0,0,-d),axis=vp.vec(0,0,3*d),shaftwidth=1E-3)
for i in range(n):
    vp.arrow(pos=L_pos[i],axis=L_dl[i])
    vp.arrow(pos=S_pos[i],axis=S_dl[i])
    
def BioSavart(i,vec_l,vec_r):
    return vec_l.cross(vec_r.norm())*i*1E-7/vec_r.mag**2

def mag_field_at_p(p,poses,dls,i):
    B=vp.vec(0,0,0)
    for k in range(n): 
        r=poses[k]-p
        B+=BioSavart(i,dls[k],r)
    return B

totalflux_sl=0
for k in range(m):
    p=vp.vec(SL_r*(k+0.5)/m,0,0.10)
    totalflux_sl+=mag_field_at_p(p,L_pos,L_dl,LL_i).dot(vp.vec(0,0,1))*S_m_area[k]
M_sl=totalflux_sl

totalflux_ls=0
for k in range(m):
    p=vp.vec(LL_r*(k+0.5)/m,0,0)
    totalflux_ls+=mag_field_at_p(p,S_pos,S_dl,SL_i).dot(vp.vec(0,0,1))*L_m_area[k]
M_ls=totalflux_ls
print(M_sl,M_ls)


# In[ ]:




