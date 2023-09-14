import matplotlib.pyplot as plt

def DDA(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1

    steps=max(abs(dx),abs(dy))

    x_inc=steps/steps
    y_inc=steps/steps

    x_point=[]
    y_point=[]

    x_point.append(x1)
    y_point.append(y1)

    for x in range(steps):
        x1=x1+x_inc
        y1=y1+y_inc

        x_point.append(x1)
        y_point.append(y1)
    


    return x_point,y_point






def main():
    x1=int(input("x1 : "))
    y1=int(input("y1 : "))
    x2=int(input("x2 : "))
    y2=int(input("y2 : "))


    x_point,y_point=DDA(x1,y1,x2,y2)

    plt.plot(x_point,y_point)
    plt.grid(which='both')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('DDA Line Drawing Algorithm')
    plt.show()


    
   


__name__ == '__main__'
main()
