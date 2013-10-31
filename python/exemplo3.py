from rpy2 import robjects as r

r.r('''
    library('lattice')
    library('Matrix')

    i <- c(1,1,2,2,3,3,3,4,4,4,5,5,5)
    j <- c(2,5,1,2,2,3,4,1,4,5,3,4,5)
    x <- c(3,1,4,1,5,9,2,6,5,3,5,8,9)
    
    AS <- sparseMatrix(i, j, x = x, giveCsparse=FALSE)
    
    v = matrix(data=(1:5), nrow=5, ncol=1)
    u <- AS %*% v
    A <- as.matrix(AS)

''')

print(r.globalenv['AS'])
print(r.globalenv['v'])
print(r.globalenv['u'])
print(r.globalenv['A'])

"""
/home/everton/.virtualenvs/rpy2/bin/python /home/everton/programacao/python/rpy2/exemplo3.py

[1,] . 3 . . 1
[2,] 4 1 . . .
[3,] . 5 9 2 .
[4,] 6 . . 5 3
[5,] . . 5 8 9

     [,1]
[1,]    1
[2,]    2
[3,]    3
[4,]    4
[5,]    5

5 x 1 Matrix of class "dgeMatrix"
     [,1]
[1,]   11
[2,]    6
[3,]   45
[4,]   41
[5,]   92

     [,1] [,2] [,3] [,4] [,5]
[1,]    0    3    0    0    1
[2,]    4    1    0    0    0
[3,]    0    5    9    2    0
[4,]    6    0    0    5    3
[5,]    0    0    5    8    9

"""