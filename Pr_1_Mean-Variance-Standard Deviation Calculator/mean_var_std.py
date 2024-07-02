import numpy as np 

def calculate(list):
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")
    
array = np.array(list).reshape(3,3)

#Calculate mean
mean_axis0=array.mean(axis=0).tolist()
mean_axis1=array.mean(axis=1).tolist()
mean_flat=array.mean().tolist()

#Calculate variance
var_axis0=array.var(axis=0).tolist()
var_axis1=array.var(axis=1).tolist()
var_flat=array.var().tolist()

#Calculate Standard Deviation
std_axis0=array.std(axis=0).tolist()
std_axis1=array.std(axis=1).tolist()
std_flat=array.std().tolist()

#Calculate Max
max_axis0=array.max(axis=0).tolist()
max_axis1=array.max(axis=1).tolist()
max_flat=array.max().tolist()

#Calculate min
min_axis0=array.min(axis=0).tolist()
min_axis1=array.min(axis=1).tolist()
min_flat=array.min().tolist()

#Calculate sum
sum_axis0=array.sum(axis=0).tolist()
sum_axis1=array.sum(axis=1).tolist()
sum_flat=array.sum().tolist()

calculations = {
    'mean': [mean_axis0, mean_axis1, mean_flat],
    'variance': [var_axis0, var_axis1, var_flat],
    'standard deviation': [std_axis0, std_axis1, std_flat],
    'max': [max_axis0, max_axis1, max_flat],
    'min': [min_axis0, min_axis1, min_flat],
    'sum': [min_axis0, min_axis1, min_flat]
}

return calculations
