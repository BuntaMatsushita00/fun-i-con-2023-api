import json
import numpy as np

def calcSum(testData):
    with open('data.json') as data:
        Data = json.load(data)

    sum = np.zeros(len(Data["Q1"]["A1"]), dtype = int)

    for i in testData["answers"]:
        tmp = np.array(Data[i["name"]][i["value"]])
        sum = sum + tmp

    result = Data["group"][(np.argmax(sum))]

    return result

def main():
    with open('test.json') as test:
        testData = json.load(test)

    result = calcSum(testData)
    print(f"あなたにおすすめな系統の壁紙は、 {result} です")

if __name__ == '__main__':
    main()
