#include <Rcpp.h>
#include <cstdlib>
#include <iostream>
#include <omp.h> 

using namespace std;

RcppExport SEXP multiplicacaoMatrizes(SEXP x, SEXP y){
  
    Rcpp::NumericMatrix matriz_1(x);
    Rcpp::NumericMatrix matriz_2(y);
    
    int nrow = matriz_1.nrow();
    int ncol = matriz_2.ncol();
    int ninner = matriz_1.ncol();
    
    Rcpp::NumericMatrix produto(nrow, ncol);

    #pragma omp parallel for
    for (int row = 0; row < nrow; row++) {
        for (int col = 0; col < ncol; col++) {
            for (int inner = 0; inner < ninner; inner++) {
                produto[(row * nrow) + col] += matriz_1[(row * nrow) + inner] * matriz_2[(inner * nrow) + col];
            }
        }
    }
    
    return produto;
}

