import numpy as np
import lmfit
import matplotlib.pyplot as plt


class gaus_fit:
    def __init__(self,pressure,type,fit_plot,fitreport,out):
        self.type = pressure
        self.type = type
        self.fit_plot = fit_plot
        self.fitreport = fitreport
        self.out = out










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

    return np.array([np.arange(von,bis,0.01),out_gaus.eval(x=np.arange(von,bis,0.01))]), out_gaus.fit_report,out_gaus

    


def gaus3fit(dat,von,bis,path,m1,m1min,m1max,m2,m2min,m2max,m3,m3min,m3max,s1=0.3,s2=0.3,s3=0.3):
    data=np.array(dat[1:4])
    vonarr = pos(von,data)
    bisarr = pos(bis,data)

    model_gaus3 = lmfit.models.GaussianModel(prefix='g1_')+lmfit.models.GaussianModel(prefix='g2_')+lmfit.models.GaussianModel(prefix='g3_')
    pars_gaus3=model_gaus3.make_params()
    pars_gaus3['g1_amplitude'].set(value=1,min=0)
    pars_gaus3['g1_center'].set(value=m1,min=m1min,max=m1max)
    pars_gaus3['g1_sigma'].set(value=s1,min=0)

    pars_gaus3['g2_amplitude'].set(value=1,min=0)
    pars_gaus3['g2_center'].set(value=m2,min=m2min,max=m2max)
    pars_gaus3['g2_sigma'].set(value=s2,min=0)

    pars_gaus3['g3_amplitude'].set(value=1,min=0)
    pars_gaus3['g3_center'].set(value=m3,min=m3min,max=m3max)
    pars_gaus3['g3_sigma'].set(value=s3,min=0)

    
    out_gaus = model_gaus3.fit(data[1,vonarr:bisarr],x=data[0,vonarr:bisarr],weights=1/data[2,vonarr:bisarr],params=pars_gaus3,nan_policy='propagate')

    
    fig = plt.figure(figsize=(8,6),dpi=80,linewidth=50)
    plt.errorbar(data[0,vonarr:bisarr],data[1,vonarr:bisarr],yerr=data[2,vonarr:bisarr],fmt='.',ecolor='gray',color='r', elinewidth=1.5, capsize=0,zorder=5,label="Daten")
    plt.plot(np.arange(von,bis,0.01),out_gaus.eval(x=np.arange(von,bis,0.01)),zorder=10,color='k',linestyle='-',alpha=1,label="Gaus-Fit")

    plt.grid()
    plt.legend()
    print(out_gaus.fit_report())
    plt.xlabel('Channel')
    plt.ylabel('Counts')

    return np.array([np.arange(von,bis,0.01),out_gaus.eval(x=np.arange(von,bis,0.01))]), out_gaus.fit_report , out_gaus




def gausfit_table(fit):
    if fit.type == 3:
        return (r"%" + str(fit.pressure) + "\n"
                r"\begin{table}[ht]" + "\n"
                r"\begin{tabular}{l|l}" + "\n"
                r"Parameter    & Value \\ \hline" + "\n"
                r"g1_amplitude &" + str(fit.out.params["g1_amplitude"].value) + r"\pm" + str(fit.out.params["g1_amplitude"].stderr) +  r"\\" + "\n"
                r"g1_center    &" + str(fit.out.params["g1_center"].value) + r"\pm" + str(fit.out.params["g1_center"].stderr) +  r"\\" + "\n"
                r"g1_sigma     &" + str(fit.out.params["g1_sigma"].value) + r"\pm" + str(fit.out.params["g1_sigma"].stderr) +  r"\\" + "\n"
                r"g2_amplitude &" + str(fit.out.params["g2_amplitude"].value) + r"\pm" + str(fit.out.params["g2_amplitude"].stderr) +  r"\\" + "\n"
                r"g2_center    &" + str(fit.out.params["g2_center"].value) + r"\pm" + str(fit.out.params["g2_center"].stderr) +  r"\\" + "\n"
                r"g2_sigma     &" + str(fit.out.params["g2_sigma"].value) + r"\pm" + str(fit.out.params["g2_sigma"].stderr) +  r"\\" + "\n"
                r"g3_amplitude &" + str(fit.out.params["g3_amplitude"].value) + r"\pm" + str(fit.out.params["g3_amplitude"].stderr) +  r"\\" + "\n"
                r"g3_center    &" + str(fit.out.params["g3_center"].value) + r"\pm" + str(fit.out.params["g3_center"].stderr) +  r"\\" + "\n"
                r"g3_sigma     &" + str(fit.out.params["g3_sigma"].value) + r"\pm" + str(fit.out.params["g3_sigma"].stderr) +  r"\\" + "\n"
                r"red\chi^2    &" + str(fit.out.redchi) + "\n"
                r"\end{tabular}" + "\n"
                r"\end{table}" + "\n")

