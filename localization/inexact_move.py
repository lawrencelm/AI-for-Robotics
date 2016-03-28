#Modify the move function to accommodate the added 
#probabilities of overshooting or undershooting 
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    
    q = []
    
    for i in range(len(p)):
        q.append(0)
    
    for i in range(len(p)):
        new_elem = p[(i-U)%len(p)]
        q[i] += new_elem*pExact
        q[(i - 1)%len(p)] += new_elem*pUndershoot
        q[(i + 1)%len(p)] += new_elem*pOvershoot
        
    return q
    

print move(p, 1)