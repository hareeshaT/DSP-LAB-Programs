p=input("enter no of rows")
q=input("enter no of columns")
mat=[ ]
for i in range (0,p):
	mat.append( [ ] )
for i in range (0,p):
	for j in range(0,q):
		mat[i].append(j)
		mat[i][j]=0
		print("entrie in row",i+1,"entrie in column",j+1)
		mat [i][j]=(input( ))
print(mat)

