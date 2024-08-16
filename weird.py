for i in range(1,100):
    i=int(input())
    if i%2!=0:
        print("Weird")
    elif i%2==0 and 6<=i<=20:
        print('Weird')
    else:
        print("Not Weird")
    break
