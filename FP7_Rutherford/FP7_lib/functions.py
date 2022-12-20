import numpy as np
import lmfit
import matplotlib.pyplot as plt

def pos(x,dat):
    for i in range(len(dat[0])):
        if np.array(dat)[0,i]>=x:
            return i
            break




def gaus1fit(dat,von,bis,path,m=1,mmin=0,mmax=2,s=0.2,smax=1000,scale=1e-9,override=False): 
    data=np.array(dat[1:4])
    vonarr = pos(von,data)
    bisarr = pos(bis,data)

    model_gaus = lmfit.models.GaussianModel()
    pars_gaus=model_gaus.guess(data=data[1,vonarr:bisarr],x=data[0,vonarr:bisarr])

    if override:
        pars_gaus["center"].set(value=m,min=mmin,max=mmax)
        pars_gaus["sigma"].set(value=1,min=0)
        pars_gaus["amplitude"].set(value=1,min=0)

    out_gaus = model_gaus.fit(data[1,vonarr:bisarr],x=data[0,vonarr:bisarr],weights=1/data[2,vonarr:bisarr],params=pars_gaus,nan_policy='propagate')

    fig = plt.figure(figsize=(8,6),dpi=80,linewidth=50)
    plt.errorbar(data[0,vonarr:bisarr],data[1,vonarr:bisarr],yerr=data[2,vonarr:bisarr],fmt='.',ecolor='gray',color='r', elinewidth=1.5, capsize=0,zorder=5,label="Daten")
    plt.plot(np.arange(von,bis,0.01),out_gaus.eval(x=np.arange(von,bis,0.01)),zorder=10,color='k',linestyle='-',alpha=1,label="Gaus-Fit")
    
    plt.grid()
    plt.legend()
    print(out_gaus.fit_report())
    plt.xlabel('Channel')
    plt.ylabel('Counts')

    return np.array([np.arange(von,bis,0.01),out_gaus.eval(x=np.arange(von,bis,0.01))]), out_gaus

    


def gaus3fit(von,bis,path):
    data=np.array(dat[1:4])
    vonarr = pos(von,data)
    bisarr = pos(bis,data)

    model_gaus3 = lmfit.models.GaussianModel(prefix='g1_')+lmfit.models.GaussianModel(prefix='g2_')+lmfit.models.GaussianModel(prefix='g3_')
    pars_gaus=model_gaus3.guess(data=data[1,vonarr:bisarr],x=data[0,vonarr:bisarr])

