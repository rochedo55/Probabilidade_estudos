from csv import reader
file = open('Apple.csv')
read = reader(file)
apps = list(list(read))
print(apps[0][0])
