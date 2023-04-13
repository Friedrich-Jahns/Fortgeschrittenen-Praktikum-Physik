import lmfit 
import numpy as np
from uncertainties import unumpy as up
from uncertainties import ufloat
import matplotlib.pyplot as plt
import pathlib


def pos(data,pos):
    for i in range(len(data)):
        if data[i]>=pos:
            return i
            break
        
def sinfit(data,x,err):
    model_sin = lmfit.models.SineModel()
    pars_sin = model_sin.guess(data=data,x=x)
    out_sin =  model_sin.fit(data,x=x,params=pars_sin,nan_policy='propagate',weights=1/np.array(err))
    return out_sin



def gausfit(data,x,err):
    model_exp = lmfit.models.GaussianModel()
    pars_exp = model_exp.guess(data=data,x=x)
    out_exp =  model_exp.fit(data,x=x,params=pars_exp,nan_policy='propagate',weights=1/np.array(err))
    return out_exp



def linfit(data,x,err):
    model_lin = lmfit.models.LinearModel()
    pars_lin = model_lin.guess(data=data,x=x)
    out_lin =  model_lin.fit(data,x=x,params=pars_lin,nan_policy='propagate',weights=1/np.array(err))
    return out_lin

def expfit(data,x,err):
    model_exp = lmfit.models.ExponentialModel()
    pars_exp = model_exp.guess(data=data,x=x)
    out_exp =  model_exp.fit(data,x=x,params=pars_exp,nan_policy='propagate',weights=1/np.array(err))
    return out_exp



def channel_to_pos(data,cal):
    slope = ufloat(cal[0],cal[1])
    intercept = ufloat(cal[2],cal[3])
    data_SI = data[0]*slope+intercept
    return [up.nominal_values(data_SI),data[1],up.std_devs(data_SI)]




def figsize(x):
    if x == 1:
        fig = plt.figure(figsize=(12,9),dpi=80,linewidth=50)
    elif x == 2:
        fig = plt.figure(figsize=(14.4,7.2),dpi=80,linewidth=50)


def form(xlim='none',grid=True,xlabel='none',ylabel='none',name='none'):
    
    if xlim != 'none':
        plt.xlim(xlim[0],xlim[1])


    plt.legend(fontsize=20)
    if xlabel == 0 :
        plt.xlabel('Test',fontsize=20)
        plt.ylabel('Test',fontsize=20)
    else:
        plt.xlabel(xlabel,fontsize=20)
        plt.ylabel(ylabel,fontsize=20)

    if grid:
        plt.grid(linestyle=':')

    if name != 'none':
        plt.savefig(name)
        plt.savefig(f'{pathlib.Path(__file__).absolute().parent.parent}/FP4_lib/plots/{name.split("/")[-1]}')
    plt.show()