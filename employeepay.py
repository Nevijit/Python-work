

list2 = [
{'name':'Mary', 'rate':15, 'hr':40},
{'name':'John','rate':22,'hr':25},
{'name':'Bob','rate':35,'hr':4},
{'name':'Mel','rate':43,'hr':62},
{'name':'Jen','rate':17,'hr':33},
{'name':'Sue','rate':29,'hr':45},
{'name':'Ken','rate':40,'hr':36},
{'name':'Dave','rate':20,'hr':17},
{'name':'Beth','rate':37,'hr':37},
{'name':'Ray','rate':16.5,'hr':80}
]
for employee in list2:
	if employee['hr'] >= 40:
		salary = 40*employee['rate'] + (employee['hr']-40)*(employee['rate']*1.5) 
	else: 
		salary = employee['rate']*employee['hr']
	print(employee['name'], " earned $ ", salary)
	
	
	




	



