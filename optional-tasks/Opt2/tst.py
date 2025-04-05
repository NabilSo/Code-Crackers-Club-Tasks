def love(n):
    heart=[]
    p = int((n)/2)
    m = int(p/2)
    d = int(n/3)
    temp = 0
    heart = [[" " for _ in range(n)] for _ in range(n)]
    for i in range(n-1,p,-1):
        heart[i][p+temp]="*"
        heart[i][p-temp]="*"
        temp+=1
    for i in range(p,m,-1):
        heart[i][n-1]="*"
        heart[i][p-temp]="*"

    j = p-temp
    temp=n-1
        
    for i in range(m,j,-1):
        heart[i][temp]="*"
        heart[i][j]="*"
        temp -= 1
        j += 1

    for i in range(2,int(p)):
        heart[i][temp]="*"
        heart[i][j]="*"
        temp -= 1
        j += 1

    for i in range(n):
        for j in range(n):
            print(heart[i][j],end=' ')
        print("")
love(30)
