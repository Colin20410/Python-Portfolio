import numpy as np


#Vector Component Initialization
     #Vector 1

while True:
 try:
   x1, y1, z1 = map(float, input("Enter first vector:").split(","))
   break
 except ValueError:
    print('Enter three numbers separated by commas')


while True:
 try:
   x2, y2, z2 = map(float, input("Enter second vector:").split(","))
   break
 except ValueError:
    print('Enter three numbers separated by commas')


    #Vector 2

#Organize Vectors
v1 = np.array([[x1,y1,z1]])
v2 = np.array([[x2,y2,z2]])


#Matrix Set up

tool = np.empty((2,3))


tool[0,:] = v1
tool[1,:] = v2

#Apply Cofactor Expansion

i_mat = tool[0:,:2]
j_mat = tool[0:,0::2]
k_mat = tool[0:, 1:]

i = np.linalg.det(i_mat)
j = np.linalg.det(j_mat)
k = np.linalg.det(k_mat)

cross = np.array([[i, j, k]])

print(f"The cross product of {v1} and {v2} is {cross}")