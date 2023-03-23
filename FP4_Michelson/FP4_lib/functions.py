import lmfit 
import numpy as np






def linfit(data,x,err):
    model_lin = lmfit.models.LinearModel()
    pars_lin = model_lin.guess(data=data,x=x)
    out_lin =  model_lin.fit(data,x=x,params=pars_lin,nan_policy='propagate',weights=1/np.array(err))
    return out_lin