m=input("enter no of rows in a matrix1")
n=input("enter no of columns in a matrix1")
mat1=[ ]
for i in range (0,m):
	mat1.append( [ ] )
for i in range (0,m):
	for j in range (0,n):
		mat1[i].append(j)
		mat1[i][j]=0
		print("entries in row",i+1,"entries in column",j+1)
		mat1 [i][j]=(input( ))
print(mat1)
p=input("enterno of rows in a matrix2")
q=input("enter no of columns in a matrix 2")
mat2=[ ]
for i in range (0,p):
	mat2.append( [ ] )
for i in range (0,p):
	for j in range (0,q):
		mat2[i].append(j)
		mat2[i][j]=0
		print("entries in row",i+1,"entries in column",j+1)
		mat2 [i][j]=(input( ))
print(mat2)
matrix=[ ]
for i in range (0,m):
	matrix.append( [ ] )
for i in range (0,m):
	for j in range (0,q):
		matrix[i].append(j)
		matrix[i][j]=0
for p in range (len(mat1)):
	for q in range (len(mat2[0])):
		for r in range(len(mat2)):
			matrix[p][q]+=mat1[p][r]*mat2[r][q]
print (matrix)
