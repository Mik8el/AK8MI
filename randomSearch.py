import matplotlib.pyplot as plt
import random
import math

def ran(start, stop, rngpct, dimz):
    step = (stop - start) / rngpct / 2
    return random.randint(0, int((stop - start) / step)) * step + start


def initVector(start, stop, rngpct, dimz):
    vekt = []
    step = (stop - start) / rngpct / 2
    for x in range(dimz):
        vekt.append(random.randint(0, int((stop - start) / step)) * step + start)
    return vekt
    

def firstDeJong(vec):
    suma = 0
    for i in range(len(vec)):
        suma = suma + (vec[i]**2)
    return suma

def secDeJong(vec):
    suma = 0
    for i in range(len(vec) - 1):
        suma = suma + (100*(((vec[i]**2)-vec[i+1])**2))+((1-vec[i])**2)
    return suma

def schwefel(vec):
    suma = 0
    for i in range(len(vec)):
        suma = suma + (-vec[i])*(math.sin(math.sqrt(abs(vec[i]))))
    return suma

def randomSearch(a, pct, dm, rep, algN = "1st"):
    myDict = {}
    if algN.lower() == '1st':
        funcName = 'firstDeJong'
    elif algN.lower() == '2nd':
        funcName = 'secDeJong'
    elif algN.lower() == 'sch':
        funcName = 'schwefel'
    titleFunc = funcName
    funcName = globals()[funcName]

    for j in range(30):
        vhodnost0 = 1000000
        x1 = []
        y1 = []
        for x in range(rep):
            vektor = initVector(-1 * a, a, pct, dm)
            vhod = funcName(vektor)
            if vhod < vhodnost0:
                vhodnost0 = vhod
                argBest = vektor.copy()
            x1.append(x)
            y1.append(vhodnost0)

        myDict[j] = y1
        plt.plot(x1, myDict[j])
   

    #for m in myDict:
        #for n in myDict.get(m):
            #print(n)
    dictlist = []
    for value in myDict.items():
        temp = [value]
        dictlist.append(temp)
    print(dictlist)
    
    plt.title("Random search -> " + titleFunc)
    plt.xlabel("Generations")
    plt.ylabel("CF value")
    plt.show()


randomSearch(500, 10, 10, 10000, 'sch')

