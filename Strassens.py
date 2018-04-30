import math as m
import time as t
import random as r
def Split(a,b,m,u):
	v=[]
	w=[]
	for j in range(m//2):
		for i in range(2):
			v.append(list(a[i][:2]))
			w.append(list(b[i][:2]))
			del(a[i][:2])
			del(b[i][:2])
		print('Splits to   2*2')
		print('\n')
		print(v)
		print(w)
		q=Strassens(v,w)
		for elements in  q:
			u.extend(elements)
		for  i in   range(2):
			del(v[0])
			del(w[0])
	for  i in  range(2):
		del(a[0])
		del(b[0])
	if len(a)==0:
		y=[]
		for i in range(n):
			y.append(u[:n])
			del(u[:n])
		print('the required matrix is')
		print(y)
		return
	else:

		Split(a,b,m,u)

def cal_power(n):
	flag=0
	while(n!=2):
		n=n/2
		if(n%2!=0):
			return False
	return True











def Strassens(a,b):
	s1=a[0][1]-b[1][1]
	s2=a[0][0]+a[0][1]
	s3=a[1][0]+a[1][1]
	s4=b[1][0]-b[0][0]
	s5=a[0][0]+a[1][1]
	s6=b[0][0]+b[1][1]
	s7=a[0][1]-a[1][1]
	s8=b[1][0]+b[1][1]
	s9=a[0][0]-a[1][0]
	s10=b[0][0]+b[0][1]
	p1=a[0][0]*s1
	p2=s2*b[1][1]
	p3=s3*b[0][0]
	p4=a[1][1]*s4
	p5=s5*s6
	p6=s7*s8
	p7=s9*s10
	r=[]
	for i in   range(2):
		r.append([])
	for  i in  range(2):
		for j in  range(1):
			if i==0:
				r[i].append(p5+p4-p2+p6)
				r[i].append(p1+p2)
			if i==1:
				r[i].append(p3+p4)
				r[i].append(p5+p1-p3-p7)
	return r

g=[]
h=[]
d=[]
print("Enter the size of the matrix  in power of 2 only")
n=int(input("Enter the size"))
if(cal_power(n)):
	for  i in range(n):
		g.append([])
		h.append([])
		for j in range(n):
			g[i].append(r.randrange(0,5,1))
			h[i].append(r.randrange(0,5,1))

	if(n==2):
		p=Strassens(g,h)
		print('The  required  matrix is')
		print(p)

	else:

		print(g)
		print(h)
		Split(g,h,n,d)
else:
	print("Not Valid power of 2")
