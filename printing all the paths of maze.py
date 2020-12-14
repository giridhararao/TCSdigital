#allPaths = []
#ind=0
def countpath(m,n):
    c=[[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        c[i][0]=1
    for j in range(n):
        c[0][j]=1
    for i in range(1,m):
        for j in range(1,n):
            c[i][j]=c[i-1][j]+c[i][j-1]
    return(c[m-1][n-1])

def findPaths(maze,m,n): 
	path = [0 for d in range(m+n-1)] 
	findPathsUtil(maze,m,n,0,0,path,0) 
	
def findPathsUtil(maze,m,n,i,j,path,indx): 
	global allPaths
	global ind
	if i==m-1: 
		for k in range(j,n):  
			path[indx+k-j] = maze[i][k] 
		#print(path)
		#allPaths.append(path)
		allPaths[ind]=path[:]
		ind+=1
		return
	if j == n-1: 
		for k in range(i,m): 
			path[indx+k-i] = maze[k][j] 
		#print(path)
		allPaths[ind]=path[:]
		ind+=1
		return
	path[indx] = maze[i][j] 
	findPathsUtil(maze, m, n, i+1, j, path, indx+1) 
	findPathsUtil(maze, m, n, i, j+1, path, indx+1) 
m,n=map(int, input().split())
b=[]
for i in range(m):
    c=[int(x) for x in input().split()]
    b.append(c)
co=countpath(m,n)
allPaths=[0 for i in range(co)]
ind=0
path=[0 for d in range(m+n-1)]
findPathsUtil(b,m,n,0,0,path,0)
#findPaths(b,m,n)
print("-----------------------------------------------------------------------------------------------")
for i in allPaths:
    print(i)
