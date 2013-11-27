#include <Rcpp.h>
#include <cstdlib>
#include <iostream>
 
using namespace std;

RcppExport SEXP comp(SEXP x, SEXP y){

    Rcpp::NumericVector vector1(x);
    Rcpp::NumericVector vector2(y);
    
    int n=vector2.size();
    Rcpp::NumericVector product(n);
    
    for(int i=0;i<n;i++){
        product[i]=vector1[i]*vector2[i];
    }
    
    return(product);
}
