import matplotlib.pyplot as plt

def bresenhams(x1,y1,x2,y2):
    x=x1
    y=y1

    dx=x2-x1
    dy=y2-y1

    dou_dy=2*dy
    diff=2*(dy-dx)
    p=2*dy-dx





    x_point=[]

    y_point=[]

    x_point.append(x)
    y_point.append(y)

    while(x<=x2):
        if(p<0):
            x=x+1
            p=p+(2*dy)
        else:
            x=x+1
            y=y+1
            p=p+(2*dy)-(2*dx)

        x_point.append(x)
        y_point.append(y)
    
    return x_point,y_point



def main():
    x1=int(input("x1 : "))
    y1=int(input("y1 : "))
    x2=int(input("x2 : "))
    y2=int(input("y2 : "))


    x_point,y_point=bresenhams(x1,y1,x2,y2)

    plt.plot(x_point,y_point,)
    plt.grid(which='both')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Bresenhams line dreawing algorithm')
    plt.show()


__name__ == '__main__'
main()
