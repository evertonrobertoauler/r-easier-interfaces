#dependencias pacotes Rcpp e cxxfunplus

codigoFibonacci <- '
    int nn = as<int>(n);
  	NumericVector xx(nn);
  	
  	for(int i=0; i<nn; i++){
    		if(i == 0 || i == 1) {
            xx[i] = i;
    		}
    		else {
            xx[i] = xx[i-1] + xx[i-2];
    		}
  	}

  	return wrap(xx);
'
fibonacci <- cxxfunction(signature(n="integer"), body=codigoFibonacci, plugin="Rcpp")
fibonacci(15)

openMPCode <- '
    std::vector<double> vetor = Rcpp::as<std::vector< double > > (v);

    #pragma omp parallel for
    for (int x = 0; x < vetor.size(); x++) {
        vetor[x] *= 3;
    }
    
    return Rcpp::wrap(vetor);
'

settings <- getPlugin("Rcpp")
settings$env$PKG_CXXFLAGS <- paste('-fopenmp', settings$env$PKG_CXXFLAGS)
settings$env$PKG_LIBS <- paste('-fopenmp -lgomp', settings$env$PKG_LIBS)
multiplicarListaPor3 <- cxxfunction(signature(v="numeric"), body=openMPCode, plugin="Rcpp", settings=settings)

sum(multiplicarListaPor3(1:10000000))


#dependencias pacotes RcppArmadillo e cxxfunplus
suppressMessages(require(inline))
code <- '
    arma::mat coeff = Rcpp::as<arma::mat>(a);
    arma::mat errors = Rcpp::as<arma::mat>(e);
    int m = errors.n_rows; int n = errors.n_cols;
    arma::mat simdata(m,n);
    simdata.row(0) = arma::zeros<arma::mat>(1,n);
    
    for (int row=1; row<m; row++) {
        simdata.row(row) = simdata.row(row-1)*trans(coeff)+errors.row(row);
    }

    return Rcpp::wrap(simdata);
'
## create the compiled function
rcppSim <- cxxfunction(signature(a="numeric",e="numeric"), code,plugin="RcppArmadillo")

a <- matrix(c(0.5,0.1,0.1,0.5),nrow=2)
e <- matrix(rnorm(10000),ncol=2)
rcppSim(a,e)