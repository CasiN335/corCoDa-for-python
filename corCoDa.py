'''Translation of corCoDa.r from the robCompositions R package


'''
import pandas as pd
import numpy as np
import math
def corCoDa(x):

    # check
    if not isinstance(x, np.ndarray) and not isinstance(x, pd.DataFrame): return "Must be a numpyarray or pandas dataframe" #otestad
    if x.any == 0: return "all elements of x must be greater than 0" #otestad
    x = pd.DataFrame(x)
    if len(x) <=2: return "calculation of average symmetric coordinates not possible"

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
        return Z_av

    ind = np.array(range(len(x.columns))) 
    corZav = pd.DataFrame(data = "NaN", index = range(len(x.columns)), columns = range(len(x.columns)))
    for i in range(0, len(x.columns)-1):
        for j in range(i+1, len(x.columns)):
            #display(np.corrcoef(balZav(x.iloc[:,[i,j, *np.delete(ind,[i,j])]])))
            corZav.iloc[i,j] = np.corrcoef(np.transpose(balZav(x.iloc[:,[i,j, *np.delete(ind,[i,j])]])))[0,1] # vi flyttar första radens andra kolumn till plats i,j
            #display(corZav)
    corZav = np.where(np.transpose(np.triu(corZav, k=1)) == 0,corZav,np.transpose(np.triu(corZav, k=1)))
    np.fill_diagonal(corZav, 1)
    return corZav