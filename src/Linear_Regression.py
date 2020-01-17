import numpy as np

def computer_error(b,w,points):
    totalerror = 0
    for i in range (0,len(points)):
        x = points[i,0]
        y = points[i,1]
        totalerror += (y-(w*x+b))**2
    return totalerror / float (len(points))

def step_gradient(b_current,w_current,points,learningrate):
    b_gradient=0
    w_gradient=0
    N =float(len(points))
    for i in range (0,len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N)*(y-((w_current*x)+b_current))
        w_gradient += -(2/N)*x*(y-((w_current*x)+b_current))
    new_b=b_current-(learningrate*b_gradient)
    new_m=w_current-(learningrate*w_gradient)
    return[new_b,new_m]

def gradientt_descent_runner(points,starting_b,starting_m,learningrate,num_iterations):
    b=starting_b
    m=starting_m
    for i in range (num_iterations):
        b,m=step_gradient(b,m,np.array(points),learningrate)
    return [b,m]

def run():
    points=np.genfromtxt("data.csv",delimiter=",")
    learningrate=0.0001
    initial_b=0
    initial_m=0
    num_iterations=1000
    print("strating gradient descent at b={0},m={1},error={2}".format(initial_b,initial_m,computer_error(initial_b,initial_m,points)))
    print("Running...")
    [b,m]=gradientt_descent_runner(points,initial_b,initial_m,learningrate,num_iterations)
    print("After{0} iterations b={1},m={2},error={3}".format(num_iterations,b,m,computer_error(b,m,points)))

if __name__ =='__main__':
    run()
