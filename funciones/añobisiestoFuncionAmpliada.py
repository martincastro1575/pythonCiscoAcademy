def isYearLeap(year):
    año = year
    if año < 1852:
        return None    
    
    if (año % 4 != 0):
        valor = False
    elif (año % 100 != 0):
        valor = True
    elif (año % 400 != 0):
        valor = False
    else:
        valor = True
    return valor
#
# tu código del laboratorio anterior
#

def daysInMonth(year, month):

    #carga en lista los meses del año
    meses = [ i for i in range(1,13)]
    
    leap_year = isYearLeap(year)
    days = 31
    if month in meses and year > 1852:
        if leap_year and month == 2:
            days = 29
        elif leap_year == False and month == 2:
            days = 28
        elif (not month % 2 and month != 8 and month != 12) or (month == 11):
            days = 30
    else:
        days = None
    
    return days

testYears = [1900, 2000, 2016, 1987]
testleapYears = [False, True, True, False]
testMonths = [2, 2, 8, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	leap_year = isYearLeap(testYears[i])
	if result == testResults[i] and leap_year == testleapYears[i]:
		print("OK")
	else:
		print("Error")
