import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError ("List must contain nine numbers.")
  else:
    array = np.array(list).reshape(3,3)
    # mean
    mean1 = np.mean(array, axis = 0).tolist()
    mean2 = np.mean(array, axis = 1).tolist()
    meanf = np.mean(array)
    # variance
    var1 = np.var(array, axis = 0).tolist()
    var2 = np.var(array, axis = 1).tolist()
    varf = np.var(array)
    # std
    std1 = np.std(array, axis = 0).tolist()
    std2 = np.std(array, axis = 1).tolist()
    stdf = np.std(array)
    # max
    max1 = np.max(array, axis = 0).tolist()
    max2 = np.max(array, axis = 1).tolist()
    maxf = np.max(array)
    # min
    min1 = np.min(array, axis = 0).tolist()
    min2 = np.min(array, axis = 1).tolist()
    minf = np.min(array)
    # sum
    sum1 = np.sum(array, axis = 0).tolist()
    sum2 = np.sum(array, axis = 1).tolist()
    sumf = np.sum(array)
    
    calculations = {
      'mean': [mean1, mean2, meanf],
      'variance': [var1, var2, varf],
      'standard deviation': [std1, std2, stdf],
      'max': [max1, max2, maxf],
      'min': [min1, min2, minf],
      'sum': [sum1, sum2, sumf]
    }
    return calculations