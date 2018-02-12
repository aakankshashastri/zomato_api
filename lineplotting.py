import matplotlib.pyplot as plt

def plotLineChart(x,y,label,color,mark):
    plt.plot(x,y,label = label,color = color,marker = mark)
    return

radius = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
area = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724]
square = [1.0, 4.0, 9.0, 16.0, 25.0, 36.0]
plotLineChart(radius,area,'circle','r','o')
plotLineChart(radius,square,'square','k','s')
#plt.plot(radius, area, label='Circle')
#plt.plot(radius, square, marker='o', linestyle='--', color='r', label='Square')
plt.xlabel('Radius/Side')
plt.ylabel('Area')
plt.title('Area of Shapes')
plt.legend()
plt.show()
