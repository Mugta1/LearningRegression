import numpy as np

#Input the training data here.
x_train=np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.2])
y_train=np.array([250, 300, 480,  430, 630, 730])


#w and b are called weights of the linear regression model.

#Function that returns mean squared error called cost of the model
def cost(x,y,w,b):
    m=x.shape[0]
    error=0
    for i in range(len(x)):
        error+=(w*x[i]+b-y[i])**2 #squared mean error 
    cost=error/(2*m)
    return cost

#Computing the derivative of the cost function with respect to w
def dj_dw(x,y,w,b):
    m=x.shape[0]
    dj_dw=0
    for i in range(len(x)):
        dj_dw+=(w*x[i]+b-y[i])*x[i]
    dj_dw= dj_dw/m
    return dj_dw
#Computing the derivative of the cost function with respect to b
def dj_db(x,y,w,b):
    m=x.shape[0]
    dj_db=0
    for i in range(len(x)):
        dj_db+=(w*x[i]+b-y[i])
    dj_db= dj_db/m
    return dj_db

#Gradient Descent Algorithm
# a is alpha, that is the learning rate
# itr is the number of iterations that the model will run
def gradient(x,y,w,b,a,itr):
    i=0
    for i in range(itr):
        temp_w= w - a*dj_dw(x,y,w,b)
        temp_b= b - a*dj_db(x,y,w,b)
        w=temp_w
        b=temp_b
    return w,b


#Final Function          
def finalfunc(x,y,w,b,a,itr):
    
    final_w,final_b=gradient(x,y,w,b,a,itr)
    #Printing the results of linear regression
    print(f'the value of w is {final_w}')
    print(f'the value of b is {final_b}')
    print(f'the cost of this function is {cost(x,y, final_w, final_b)}')
    #Using the results of linear regression to find values. 
    while True:

        user=float(input("For what area of house would you like to find the selling price?"))
        if user<=0.0:
            print(f'You want to calculate the price of a house with area {user}? what idiot la')
            c=int(input("Do you want to continue?\n 1.Press 0 to end the program,\n 2.Press 1 to Continue"))
            if c==0:
                break
        else:
            print(f"the selling price of a house with area {user} is equal to {final_w*user+b}")
            break

#Calling the final function
finalfunc(x_train,y_train,200,100,0.1,3773)

#You can input your own values for w,b,a,itr

