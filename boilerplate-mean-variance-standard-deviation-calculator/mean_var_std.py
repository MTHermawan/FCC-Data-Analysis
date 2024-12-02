import numpy as np

def GetMean(list, axis = -1):
    if axis >= 0:
        mean = np.ndarray.tolist(np.mean(list, axis))
    else:
        mean = np.mean(list.flatten())
    return mean

def GetVar(list, axis = -1):
    if axis >= 0:
        variance = np.ndarray.tolist(np.var(list, axis))
    else:
        variance = np.var(list.flatten())
    return variance

def GetStd(list, axis = -1):
    if axis >= 0:
        std = np.ndarray.tolist(np.std(list, axis))
    else:
        std = np.std(list.flatten())
    return std

def GetMax(list, axis = -1):
    if axis >= 0:
        max = np.ndarray.tolist(np.max(list, axis))
    else:
        max = np.max(list.flatten())
    return max

def GetMin(list, axis = -1):
    if axis >= 0:
        min = np.ndarray.tolist(np.min(list, axis))
    else:
        min = np.min(list.flatten())
    return min

def GetSum(list, axis = -1):
    if axis >= 0:
        sum = np.ndarray.tolist(np.sum(list, axis))
    else:
        sum = np.sum(list.flatten())
    return sum

def calculate(list):
    # The input of the function should be a list containing 9 digits.
    if np.size(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Define the calculations dictionary
    calculations = {}

    # Reshape the list into a 3x3 matrix
    matrix = np.reshape(list, (3,3))

    meanAxis1 = GetMean(matrix, 0)
    meanAxis2 = GetMean(matrix, 1)
    meanFlat = GetMean(matrix)

    varAxis1 = GetVar(matrix, 0)
    varAxis2 = GetVar(matrix, 1)
    varFlat = GetVar(matrix)

    stdAxis1 = GetStd(matrix, 0)
    stdAxis2 = GetStd(matrix, 1)
    stdFlat = GetStd(matrix)

    maxAxis1 = GetMax(matrix, 0)
    maxAxis2 = GetMax(matrix, 1)
    maxFlat = GetMax(matrix)

    minAxis1 = GetMin(matrix, 0)
    minAxis2 = GetMin(matrix, 1)
    minFlat = GetMin(matrix)

    sumAxis1 = GetSum(matrix, 0)
    sumAxis2 = GetSum(matrix, 1)
    sumFlat = GetSum(matrix)

    calculations['mean'] = [meanAxis1, meanAxis2, meanFlat]
    calculations['variance'] = [varAxis1, varAxis2, varFlat]
    calculations['standard deviation'] = [stdAxis1, stdAxis2, stdFlat]
    calculations['max'] = [maxAxis1, maxAxis2, maxFlat]
    calculations['min'] = [minAxis1, minAxis2, minFlat]
    calculations['sum'] = [sumAxis1, sumAxis2, sumFlat]

    return calculations