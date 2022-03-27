x=[[1,3],
   [7,9]]
y=[[4,6],
   [7,8]]
r=[[0,0],
   [0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            r[i][j]+= x[i][k] * y[k][j]

for h in r:
 print(h)


