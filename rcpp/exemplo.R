dyn.load('/home/everton/Faculdade/6_semestre/Computação Cientifica/R_Easier_Interfaces/rcpp/exemplo.so')

# teste openmp
nrColl = 1000
nrNrs = nrColl * nrColl

mat_1 <- matrix(rep(1:1, each = nrNrs), nc = nrColl)
mat_2 <- matrix(rep(1:1, each = nrNrs), nc = nrColl)
sum(.Call('multiplicacaoMatrizes', mat_1, mat_2))

# teste multiplicacao
mat_1 <- matrix(rep(1:10, each = 10), nc = 10)
mat_2 <- matrix(rep(1:10, times = 10), nc = 10)
.Call('multiplicacaoMatrizes', mat_1, mat_2)