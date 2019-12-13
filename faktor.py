import os, sys

print('\n', "  • Mencari Bilangan Faktor •")

def faktor(x):
	print('\n[•] Faktor dari', x, 'adalah: ')
	for i in range(1, x+1):
		if x % i == 0:
			print('\n-', i)

num = int(input('\n[•] Inputkan bilangan: '))

faktor(num)

quest = input("\n[Quest] Ingin kembali ke menu? y/n: ")

if quest == 'y' or quest == 'Y':
	os.system("python math.py")

else:
	print("\n ` Terima Kasih ^_^")