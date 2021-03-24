#funcion con codigo de prueba


def isYearLeap(year):
    año = year
    
    if (año % 4 != 0):
        valor = False
    elif (año % 100 != 0):
        valor = True
    elif (año % 400 != 0):
        valor = False
    else:
        valor = True
    return valor

#resultado de prueba
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
