import re
f = 'toy_dataset.csv'

#Все столбики, кроме первого

def getCity(line):
    result = re.split(r',',line, maxsplit = 2)
    city = result[1].capitalize()
    return city, result[2]

def getGender(line):
    result = re.split(r',', line, maxsplit = 1)
    gender = result[0].capitalize()
    return gender, result[1]

def getAge(line):
    result = re.split(r',', line, maxsplit = 1)
    age = re.findall(r'\d{1,3}', result[0])
    return age[0], result[1]

def getIncome(line):
    result = re.split(r',', line, maxsplit = 1)
    income = re.findall(r'\d{1,6}\.\d{1,5}', result[0])
    return income[0], result[1]

def getIllness(line):
    illness = re.split(r',', line, maxsplit=1)
    return illness[0]


try:
    with open(f, encoding = 'utf-8', mode = 'r') as file:

        file.readline()
        line_number = 1
        dct = {}
        incomeDict = {}
        a = []

        for line in file:
            line = line.strip().rstrip()
            line_number += 1
            if not line:
                continue


            city, line = getCity(line)
            gender, line = getGender(line)
            age, line = getAge(line)
            income, line = getIncome(line)
            illness = getIllness(line)
            c = 0
            a.append(gender)
            dct[city] = a
            c += float(income)
            if age in incomeDict.keys():
                d = incomeDict[age]
                d += c
                incomeDict[age] = d
            else:
                incomeDict[age] = c
#dct - словник формату {"місто": "стать"}, incomeDict - словник, що містить інформацію про загальний прибуток людей одного віку

            print(city, gender, age, income, illness)

except IOError as e:
   print ("I/O error({0}): {1}".format(e.errno, e.strerror))

except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))