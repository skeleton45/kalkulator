#lagi belajar python slur ~

import os,sys
os.system("clear")

print "\033[32;1mwww.affan45.site"

print ('  ')

a = input("\033[37;1mMasukan Bilangan Pertama  : ")
b = input("\033[37;1mMasukan Bilangan Kedua    : ")
c = a+b
d = a-b
e = a*b
f = a/b
g = a**b
print '   '

print ("\033[33;1mIngin di apakan bilangan ini?\n\n1. TAMBAH\n2. KURANG\n3. KALI\n4. BAGI\n5. PEMANGKATAN")

print '   '

p = int(input("\033[36;;1mPilihanmu: "))
print '  '
if p == 1:
	print "\033[37;1mHasil: " , c
if p == 2:
	print "\033[37;1mHasil: " , d
if p == 3:
	print "\033[37;1mHasil: " , e
if p == 4:
	print "\033[37;1mHasil: " , f
if p == 5:
	print "\033[37;1mHasil: " , g
	
q = raw_input("\nIngin menghitung lagi? y/n: ")
if q == "y":
		os.system("python2 kalkulator.py")
