import numpy as np
import matplotlib.pyplot as plt
import random

def ball_pickup():
    ball = random.randint(0,1)
    return ball
def random_balls(start_vector, transition_matrix, steps):
    # start_vector = en vektor [n0, m0] där 
    # n0 är röda och m0 blåa bollar i urnan från början
    # transition_matrix = en övergångsmatris som talar
    # om sannolikheten att plocka upp en boll vid varje step
    red = []
    blue = []
    for i in range(steps):
        ball = ball_pickup()
        if ball == 0:
            start_vector = start_vector + transition_matrix[0]
            red.append(start_vector[0])
            blue.append(start_vector[1])
        else:
            start_vector = start_vector + transition_matrix[1]
            red.append(start_vector[0])
            blue.append(start_vector[1])
           
    return start_vector, red, blue 

start_vector = np.array([1,1])
transition_matrix = np.array([[2,0],
                              [0,2]])
t = np.linspace(0,100,100)
a = random_balls(start_vector, transition_matrix, 100)


plt.plot(t, a[2] ,linestyle = 'solid', color='blue', label = 'blåa bollar')
plt.plot(t, a[1] ,linestyle = 'solid', color='red', label = 'röda bollar')
plt.xlabel('steps')
plt.title('antal')
plt.legend(loc='upper right')
plt.show()  
       

        
        
        
    