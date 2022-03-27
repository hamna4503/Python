x=[[1,20,3],
   [6,70,8],
   [9,8,70]]
y=[[9,8,7],
   [4,3,2],
   [1,2,3]]
r=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        r[i][j]=x[i][j]+y[i][j]

for i in r:
    print(i)
