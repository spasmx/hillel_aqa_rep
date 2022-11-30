# Given two sets A and B
# Set A contains the names of debtors for September
# Set B contains the names of debtors for October
# Find:
# * Display the names of people who are due for September and October
# * Display debtors for October who have no debt for September

debtors_sept = {'James', 'Mary', 'Robert', 'Patricia', 'Michael', 'Susan', 'Charles'}
debtors_oct = {'Richard', 'Sarah', 'Mary', 'Elizabeth', 'James', 'Charles', 'Kenneth'}

debtors_all = debtors_sept.intersection(debtors_oct)
debtors_oct_only = debtors_oct.difference(debtors_sept)

print(debtors_all)
print(debtors_oct_only)
