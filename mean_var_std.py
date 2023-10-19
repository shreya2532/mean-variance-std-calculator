import numpy as np

def calculate (numbers):
    if len(numbers)!= 9:
        raise ValueError("List must contain nine numbers")
    
    arr = np.array(numbers).reshape(3,3)
    mean = [list(arr.mean(axis=0)), list(arr.mean(axis = 1)), arr.mean()]
    variance = [list(arr.var(axis=0)), list(arr.var(axis = 1)), arr.var()]
    stdd = [list(arr.std(axis=0)), list(arr.std(axis = 1)), arr.std()]
    maxx = [list(arr.max(axis=0)), list(arr.max(axis = 1)), arr.max()]
    minn = [list(arr.min(axis=0)), list(arr.min(axis = 1)), arr.min()]
    summ = [list(arr.sum(axis=0)), list(arr.sum(axis = 1)), arr.sum()]

    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': stdd,
        'max': maxx,
        'min': minn,
        'sum': summ
    }
    
    return result