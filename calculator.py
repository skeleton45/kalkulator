import os, sys

print ("\n  • Kalkulator Sederhana •")

print ('''
1. Kali
2. Bagi
3. Tambah
4. Kurang
''')

pilih = int(input("[Choice] > "))

if pilih == 1:
	a = int(input("\n[•] Masukan bilangan: "))
	b = int(input("[•] Masukan bilangan: "))
	print("\n[•] Hasil: " , a*b)

elif pilih == 2:
	b = int(input("\n[•] Masukan bilangan: "))
	c = int(input("[•] Masukan bilangan: "))
	print("\n[•] Hasil: " , b/c)

elif pilih == 3:
	d = int(input("\n[•] Masukan bilangan: "))
	e = int(input("[•] Masukan bilangan: "))
	print("\n[•] Hasil: ", d+e)

elif pilih == 4:
	f = int(input("\n[•] Masukan bilangan: "))
	g = int(input("[•] Masukan bilangan: "))
	print("\n[•] Hasil: " , f-g)

else:
	print("\n[Error] Input pilihan yang benar!")
	os.system("python calculator.py")
	
q = input("\n[Quest] Kembali ke menu? y/n: ")

if q == 'y' or q == 'Y':
	os.system("python math.py")
	
else:
	print("\n` Terima kasih ^_^")