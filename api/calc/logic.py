import json
import numpy as np

def calcSum(input):
    with open("api/data/data.json") as data:
        Data = json.load(data)

    sum = np.zeros(len(Data["Q1"]["A1"]), dtype = int)

    for i in input.answers:
        tmp = np.array(Data[i.name][i.value])
        sum = sum + tmp

    result = Data["group"][(np.argmax(sum))]

    return result

def main(input):
    result = calcSum(input)
    return result

