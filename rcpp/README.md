# Exemplo com Rcpp para utilizar funcoes C++ no R

Para compilar o programa exemplo.cpp basta rodar os seguintes comandos em um terminal linux.

    export PKG_LIBS='`Rscript -e "Rcpp:::LdFlags()"` -fopenmp -lgomp'
    export PKG_CXXFLAGS='`Rscript -e "Rcpp:::CxxFlags()"` -fopenmp'
    R CMD SHLIB exemplo.cpp

Para compilar exemplo2.cpp sem openmp

    export PKG_CXXFLAGS=`Rscript -e "Rcpp:::CxxFlags()"`
    export PKG_LIBS=`Rscript -e "Rcpp:::LdFlags()"`
    R CMD SHLIB exemplo2.cpp
