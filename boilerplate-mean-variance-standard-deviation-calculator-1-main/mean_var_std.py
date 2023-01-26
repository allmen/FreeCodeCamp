import numpy as np

def calculate(list):
    if len(list) == 9:
        npList = np.array(list).reshape(-1, 3)
        meanR = np.mean(npList, axis=0).tolist()
        meanC = np.mean(npList, axis=1).tolist()
        meanA = np.mean(npList).tolist()
        varR = np.var(npList, axis=0).tolist()
        varC = np.var(npList, axis=1).tolist()
        varA = np.var(npList).tolist()
        stdR = np.std(npList, axis=0).tolist()
        stdC = np.std(npList, axis=1).tolist()
        stdA = np.std(npList).tolist()
        maxR = np.max(npList, axis=0).tolist()
        maxC = np.max(npList, axis=1).tolist()
        maxA = np.max(npList).tolist()
        minR = np.min(npList, axis=0).tolist()
        minC = np.min(npList, axis=1).tolist()
        minA = np.min(npList).tolist()
        sumR = np.sum(npList, axis=0).tolist()
        sumC = np.sum(npList, axis=1).tolist()
        sumA = np.sum(npList).tolist()

        calculations =\
        {
            'mean' : [meanR,meanC,meanA],
            'variance' : [varR,varC,varA],
            'standard deviation' : [stdR,stdC,stdA],
            'max' : [maxR, maxC, maxA],
            'min' : [minR, minC,minA],
            'sum' : [sumR,sumC, sumA]
        }

        return calculations
    else:
        raise ValueError("List must contain nine numbers.");

print(calculate([2,6,2,8,4,0,1,5,7]))

