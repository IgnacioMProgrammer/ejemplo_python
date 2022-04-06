import string
from tkinter import N 
evaluar = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems. However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modelin system that can exploit the largest HPC resources and emerging computing architectures. """


listaEvaluar= evaluar.split('\n')
listaEvaluar[0]=listaEvaluar[0].split(' ')

listaEvaluar[1]=listaEvaluar[1].split('.')
    
i=0
for lista in listaEvaluar[1]:
    listaEvaluar[1][i]= lista.split(" ")
titulo = (len(listaEvaluar[0])< 11)
print("El titulo es facil de leer:"+str(titulo))
facil=0
aceptable=0
dificil=0
muy_Dificil=0
for lista in listaEvaluar[1]:
    if(len(lista)<25):
        if(len(lista)<13):
            facil+=1
        elif(len(lista)<18):
            aceptable+=1
        else:
            dificil+=1    
    else:
        muy_Dificil+=1
print(f"facil:{facil} aceptable:{aceptable} dificil:{dificil} muy-dificil{muy_Dificil}")


#print(listaEvaluar[1])    
