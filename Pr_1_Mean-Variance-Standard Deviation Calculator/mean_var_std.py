import numpy as np 

def calculate(list):
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")
    
array = np.array(list).reshape(3,3)

#Calculate mean
mean_axis0=array.mean(axis=0).tolist()
mean_axis1=array.mean(axis=1).tolist()
mean_flat=array.mean().tolist()
