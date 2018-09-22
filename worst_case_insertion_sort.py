def insertion_sort (data):
   j=1
   while j<len(data)
    key=data(j)
    i=j-1
    while i> -1 and data(i)>key:
        data[i+1]=data[i]
        i=i-1
    data[i+1]=key
    j+=1
iterations=[10,100,1000,10000]
time_list=[1,2,3,4]
for n in range(4):
    data=list(range(1,iterations[n]))
    data.sort(reverse=True)
    start=time.time()
    insertion_sort(data)
    time_consumption=time.time()-start
    time_list[n]=time_consumption
    print('time: '+'{0:.9f}'.format(time_list[n])+ ' seconds')
    n=n+1
    
