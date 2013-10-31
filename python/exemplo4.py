from rpy2 import robjects as r

r.globalenv['a'] = r.IntVector([1, 2, 3])

r.r('''
    b <- rep(a, times=3, each=2)
''')

print(r.globalenv['b'])

"""
/home/everton/.virtualenvs/rpy2/bin/python /home/everton/programacao/python/rpy2/exemplo4.py

 [1] 1 1 2 2 3 3 1 1 2 2 3 3 1 1 2 2 3 3

"""