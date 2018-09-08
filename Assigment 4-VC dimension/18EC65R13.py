import numpy as np
import matplotlib.pyplot as plt
def gaussian(x,mean,sd):
    return (np.exp( -((x-mean)*(x-mean))/(2*sd*sd)))

t=np.linspace(16,48,321)

TE_malignant= gaussian(t,37,1)
TE_benign=gaussian(t,32,4)
TE_tpf=np.zeros(t.size)
TE_fpf=np.zeros(t.size)
C_tpf=np.zeros(t.size)
C_fpf=np.zeros(t.size)
C_malignant = gaussian(t,37,2)
C_benign = gaussian(t,32,3)

threshold=0

while(threshold<t.size):
    TE_tpf[threshold]=(TE_malignant[threshold:].sum()/TE_malignant.sum())
    TE_fpf[threshold]=(TE_benign[threshold:].sum()/TE_benign.sum())
    C_tpf[threshold]=(C_malignant[threshold:].sum()/C_malignant.sum())
    C_fpf[threshold]=(C_benign[threshold:].sum()/C_benign.sum())
    print("Calculated for threshold={}".format(threshold))
    threshold=threshold+1


threshold=0
TE_area=0.0
C_area=0.0
while(threshold<t.size-1):
    TE_area=TE_area+(TE_tpf[threshold]*(TE_fpf[threshold]-TE_fpf[threshold+1]))
    C_area=C_area+(C_tpf[threshold]*(C_fpf[threshold]-C_fpf[threshold+1]))
    threshold=threshold+1

print("Third Eye Area Under Curve={}".format(TE_area))
print("Competitor Eye Area Under Curve={}".format(C_area))
if(TE_area>C_area):
    print("Third Eye Solution is better")
else:
    print("Competitor Solution is better")    
plt.plot(TE_fpf,TE_tpf,'r',label='Third Eye Solution')
plt.plot(C_fpf,C_tpf,'b',label="Competetor's Solution")
plt.legend(loc='lower right')
plt.ylabel("TPF")
plt.xlabel("FPF")
plt.show()