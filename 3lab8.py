def even(a):
    i=1
    l=[]
    while i <=a:
       if i%2 == 0 or i%3==0:
         l.append(str(i))

       i+=1
    h=" "
    for i in l:
        h+=i+","
    print(h)

even(20)
