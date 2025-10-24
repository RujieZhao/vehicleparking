
import numpy as np

path = "cadiliac_3d.txt"


with open(path,"r") as f:
    data = f.read()
print(len(data),data[0])
data = data.split(" ")[3:]
data[0] = data[0][9:]
print(data[0])
length = len(data)
print(length)
if length % 3 ==0:
    caliliac = [[[]for j in range(3)] for i in range(length//3)]
    print(len(caliliac),len(caliliac[0]))
    for i in range(int(length/3)):
        for j in range(3):
            ind = i*3+j
            caliliac[i][j] = float(data[ind][:-1])
for i in range(10):
    print(caliliac[i])





#
# data = np.loadtxt("cadiliac_3d.txt")
# print(data.shape)








