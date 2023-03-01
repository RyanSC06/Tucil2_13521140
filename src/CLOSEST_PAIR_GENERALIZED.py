#NIM: 13521140
#Nama: Ryan Samuel Chandra
#Mata Kuliah: IF2211 Strategi Algoritma
#Topik: Tugas Kecil 2
#Tanggal: Rabu, 1 Maret 2023

#Program CLOSEST_PAIR_GENERALIZED
#Spesifikasi : Program untuk mencari pasangan-pasangan titik acak yang jaraknya terdekat dalam sumbu
#              dimensi N, menggunakan perhitungan jarak euclidean dengan algoritme brute force,
#              kemudian dibandingkan secara langsung dengan algoritme divide and conquer

#DEKLARASI LIBRARY
import random
import time
from FUNCTIONS import *

#KAMUS GLOBAL
# n, N : int
# points_list : array[0..n-1] of array[0..2] of int
# min_dist_list : array[0..?] of array[0..1] of array[0..2] of int
# min_dist_list2 : array[0..?] of array[0..1] of array[0..2] of int
# point : array[0..2] of int (pencacah list of list)
# i : int (pencacah)
# minimum, minimum2 : float
# num_of_calc, num_of_calc2 : int
# start_time1, time1 : time (dari library)
# start_time2, time2 : time (dari library)
# question : char
    

#TAMPILAN AWAL
print("\n")
print(" ██████╗██╗      ██████╗ ███████╗███████╗███████╗████████╗   ██████╗  █████╗ ██╗██████╗") 
print("██╔════╝██║     ██╔═══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝   ██╔══██╗██╔══██╗██║██╔══██╗")
print("██║     ██║     ██║   ██║███████╗█████╗  ███████╗   ██║█████╗██████╔╝███████║██║██████╔╝")
print("██║     ██║     ██║   ██║╚════██║██╔══╝  ╚════██║   ██║╚════╝██╔═══╝ ██╔══██║██║██╔══██╗")
print("╚██████╗███████╗╚██████╔╝███████║███████╗███████║   ██║      ██║     ██║  ██║██║██║  ██║")
print(" ╚═════╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝      ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝\n")
                                                                                        

#INISIALISASI
N = 0
n = 0

while (N < 1):
    N = int(input("Masukkan dimensi: "))
    if (N < 1):
        print("Masukan harus lebih besar dari 0")
while (n < 2):
    n = int(input("Masukkan jumlah titik: "))
    if (n < 2):
        print("Masukan harus lebih besar dari 1")
points_list = [[(round(random.uniform(-50.00,50.00), 2)) for j in range(N)] for i in range(n)]


#PROGRAM UTAMA
question = 'x'
while (question != '0' and question != '1'):
    question = str(input("\nApakah Anda ingin mencetak titik-titik Anda? (0/1): "))
    if (question != '0' and question != '1'):
        print("Masukkan '0' untuk tidak, atau '1' untuk ya")

if (question == '1'):
    print("\nTitik:")
    for point in (points_list):
        print(point)
    
# ------------------------BRUTE FORCE------------------------
start_time1 = time.time()
minimum, num_of_calc, min_dist_list = closest_pair_BF(points_list, n)
time1 = time.time() - start_time1
# -----------------------------------------------------------

# --------------------DIVIDE AND CONQUER---------------------
quick_sort(points_list, 0, len(points_list)-1, 0)
start_time2 = time.time()
minimum2, num_of_calc2, min_dist_list2 = closest_pair_generalized(points_list, n, N)
time2 = time.time() - start_time2
# -----------------------------------------------------------


#MENCETAK KE LAYAR
print("\n================================================")
print("                   BRUTE FORCE                  ")
print("================================================")
print("Jarak dua titik terdekat: %.5f satuan," % minimum)
print("yaitu antara titik: ", end='')
for i in range(len(min_dist_list)):
    print("\n", min_dist_list[i][0], "dan", min_dist_list[i][1])

print("\nWaktu komputasi: %.10f detik" % (time1))
print("Jumlah perhitungan = {0}({1}-1)/2 = {2}".format(n, n, num_of_calc))


print("\n================================================")
print("               DIVIDE AND CONQUER               ")
print("================================================")
print("Jarak dua titik terdekat: %.5f satuan," % minimum2)
print("yaitu antara titik: ", end='')
for i in range(len(min_dist_list2)):
    print("\n", min_dist_list2[i][0], "dan", min_dist_list2[i][1])

print("\nWaktu komputasi: %.10f detik" % (time2))
print("Jumlah perhitungan =", num_of_calc2)

print("\nTerima kasih sudah menggunakan layanan ini :)")
