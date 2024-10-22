'''Translation of corCoDa.r to python (from the robCompositions R package)

corCoDa.py v1.2
- fixed transpose of 0.000000 causing NaN values

ORIGINAL AUTHOR: Petra Kynclova
#' Correlations for compositional data
#' 
#' This function computes correlation coefficients between compositional parts based
#' on symmetric pivot coordinates.
#' 
#' @param x a matrix or data frame with compositional data
#' @param ... additional arguments for the function \code{\link{cor}}
#' @return A compositional correlation matrix.
#' @author Petra Kynclova
#' @export
#' @examples
#' data(expenditures)
#' corCoDa(expenditures)
#' @references Kynclova, P., Hron, K., Filzmoser, P. (2017)
#' Correlation between compositional parts based on symmetric balances.
#' \emph{Mathematical Geosciences}, 49(6), 777-796.
#' @examples
#' x <- arcticLake 
#' corCoDa(x)
#' 
'''
import pandas as pd
import numpy as np
import math
def corCoDa(x, **kwargs):

    # check
    if not isinstance(x, np.ndarray) and not isinstance(x, pd.DataFrame): raise ValueError("Must be a numpyarray or pandas dataframe")
    x = pd.DataFrame(x)
    if (x.select_dtypes(include=['object']).empty == False) or (x <= 0).values.any() or x.isnull().values.any(): raise ValueError("all elements of x must be greater than 0") 
    if len(x.columns) <=2: raise ValueError("calculation of average symmetric coordinates not possible")

    def balZav(x):
        D = len(x.columns)
        Z_av = np.full((len(x),2), np.nan)
        p1 = math.sqrt(D-1+math.sqrt(D*(D-2)))/math.sqrt(2*D)

        if(D==3):
            p2 = x.iloc[:,2]
        else:
            p2 = x.iloc[:,2:D].product(axis = 1)

        p3 = (math.sqrt(D-2)+math.sqrt(D))/(math.sqrt(D-2)*(D-1+math.sqrt(D*(D-2))))
        p4 = 1/(D-1+math.sqrt(D*(D-2)))
        Z_av[:,0] = p1*(np.log(x.iloc[:,0]/(x.iloc[:,1]**p4 * p2**p3)))
        Z_av[:,1] = p1*(np.log(x.iloc[:,1]/(x.iloc[:,0]**p4 * p2**p3)))
        Z_av = pd.DataFrame(Z_av)
        return Z_av

    ind = np.array(range(len(x.columns))) 
    corZav = pd.DataFrame(data = "NaN", index = range(len(x.columns)), columns = range(len(x.columns)))
    for i in range(0, len(x.columns)-1):
        for j in range(i+1, len(x.columns)):
            corZav.iloc[i,j] = balZav(x.iloc[:,[i,j, *np.delete(ind,[i,j])]]).corr(**kwargs).iloc[0,1] # correlations for average coordinates Z.av
    corZav = np.where(np.transpose(np.triu(corZav, k=1)) == 0,corZav,np.transpose(np.triu(corZav, k=1)))
    np.fill_diagonal(corZav, 1)
    corZav = pd.DataFrame(corZav).astype('float64')
    corZav = corZav.replace(np.nan,0)
    return corZav
