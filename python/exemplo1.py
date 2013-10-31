from rpy2 import robjects as r

print("Titanic:")
print(r.r('Titanic'))

r.r('''
    f <- function(r, verbose=FALSE) {
        if (verbose) {
            cat("I am calling f().\n")
        }
        2 * pi * r
    }
    b <- f(10)
''')

print("Representacao funcao f:")
print(r.globalenv['f'].r_repr())

print("Valor da variavel b:")
print(r.globalenv['b'])

"""
/home/everton/.virtualenvs/rpy2/bin/python /home/everton/programacao/python/rpy2/exemplo1.py

Titanic:
, , Age = Child, Survived = No

      Sex
Class  Male Female
  1st     0      0
  2nd     0      0
  3rd    35     17
  Crew    0      0

, , Age = Adult, Survived = No

      Sex
Class  Male Female
  1st   118      4
  2nd   154     13
  3rd   387     89
  Crew  670      3

, , Age = Child, Survived = Yes

      Sex
Class  Male Female
  1st     5      1
  2nd    11     13
  3rd    13     14
  Crew    0      0

, , Age = Adult, Survived = Yes

      Sex
Class  Male Female
  1st    57    140
  2nd    14     80
  3rd    75     76
  Crew  192     20


Representacao funcao f:
function (r, verbose = FALSE)
{
    if (verbose) {
        cat("I am calling f().\n")
    }
    2 * pi * r
}

Valor da variavel b:
[1] 62.83185

"""