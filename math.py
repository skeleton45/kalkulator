import os, sys

os.system("clear")

print("""
  Program Matematika Sederhana
        Coded by Affan R
      
1. Aritmatika
2. Mencari Faktor Bilangan
3. Request Module
""")

choice = int(input("[Choice] > "))

if choice == 1:
	os.system("python calculator.py")

elif choice == 2:
	os.system("python faktor.py")

#elif choice == 3:
	
else:
	print("\n[Error] Input pilihan yang benar!")