#NIM: 13521140
#Nama: Ryan Samuel Chandra
#Mata Kuliah: IF2211 Strategi Algoritma
#Topik: Tugas Kecil 2
#Tanggal: Sabtu, 25 Februari 2023

#Program FUNCTIONS
#Spesifikasi : Program berisi fungsi-fungsi pendukung untuk melakukan pencarian closest-pair dari
#              titik-titik acak dengan menggunakan algoritme brute force dan divide and conquer

#DEKLARASI LIBRARY
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#DEKLARASI FUNGSI DAN PROSEDUR
# calculate_distance(point1, point2)
# partition(points_list, start, end, axis)
# quick_sort(points_list, start, end, axis)
# closest_pair(points_list, num)
# closest_pair_generalized(points_list, num, dimension)
# closest_pair_BF(points_list, n)
# print3D(points_list, min_dist_list)


#IMPLEMENTASI FUNGSI DAN PROSEDUR
def calculate_distance(point1, point2):
    #Menghitung jarak euclidean antara point1 dan point2
#KAMUS LOKAL
    # point1, point2 : array[0..?] of int
    # i : int (pencacah)
    # distance : float
#ALGORITME
    distance = 0.0
    for i in range(len(point1)):
        distance = distance + (point1[i]-point2[i])**2

    distance = math.sqrt(distance)
    return (distance)


def partition(points_list, start, end, axis):
    #Mempartisi senarai berisi koordinat titik menjadi
    #dua bagian berdasarkan axis (absis / ordinat)
#KAMUS LOKAL
    # points_list : array[0..?] of array[0..?] of int
    # start, end : int (indeks awal dan akhir points_list)
    # axis : int (0 berarti sumbu x, 1 berarti sumbu y)
    # pivot : int
    # i, j : int
#ALGORITME
    pivot = points_list[end][axis]
    i = start - 1

    for j in range(start, end):
        if (points_list[j][axis] <= pivot):
            i = i + 1
            (points_list[i], points_list[j]) = (points_list[j], points_list[i])

    (points_list[i+1], points_list[end]) = (points_list[end], points_list[i+1])
    return (i+1)


def quick_sort(points_list, start, end, axis):
    #Mengurutkan senarai berisi koordinat titik berdasarkan axis (absis / ordinat)
#KAMUS LOKAL
    # points_list : array[0..?] of array[0..?] of int
    # start, end : int (indeks awal dan akhir points_list)
    # axis : int (0 berarti sumbu x, 1 berarti sumbu y)
    # mid : int
#ALGORITME
    if (start < end):
        mid = partition(points_list, start, end, axis)
        quick_sort(points_list, start, mid-1, axis)
        quick_sort(points_list, mid+1, end, axis)


def closest_pair(points_list, num):
    #Mencari pasangan-pasangan titik acak dalam points_list yang jaraknya terdekat
    #dengan menggunakan algoritme divide and conquer. Prasyarat: points_list harus
    #sudah dalam keadaaan terurut menaik pada absisnya; titik berdimensi tiga
#ALGORITME
    min_dist_list = []
    if (num == 3):
        minimum, num_of_calc, min_dist_list = closest_pair_BF(points_list, num)
    elif (num == 2):
        minimum = calculate_distance(points_list[0], points_list[1])
        num_of_calc = 1
        min_dist_list.append([points_list[0], points_list[1]])
    else:
        points_list1 = []
        points_list2 = []
        
        for i in range(0, num//2, 1):
            points_list1.append(points_list[i])
        for i in range(num//2, num, 1):
            points_list2.append(points_list[i])

        minimum1, num_of_calc1, min_dist_list1 = closest_pair(points_list1, num//2)
        minimum2, num_of_calc2, min_dist_list2 = closest_pair(points_list2, num//2)
        num_of_calc = num_of_calc1 + num_of_calc2
        
        if (minimum1 < minimum2):
            minimum = minimum1
            min_dist_list = min_dist_list1
        elif (minimum2 < minimum1):
            minimum = minimum2
            min_dist_list = min_dist_list2
        else: #minimum1=minimum2
            minimum = minimum1
            min_dist_list = min_dist_list1 + min_dist_list2

        #Perhitungan dalam "STRIP"
        additional_list1 = []
        additional_list2 = []
        for point in points_list1:
            if (point[0] >= points_list[num//2 - 1][0] - minimum):
                additional_list1.append(point)
        for point in points_list2:
            if (point[0] <= points_list[num//2 - 1][0] + minimum):
                additional_list2.append(point)

        for i in range(0, len(additional_list1), 1):
            for j in range(0, len(additional_list2), 1):
                if (abs(additional_list1[i][0] - additional_list2[j][0]) > minimum
                or abs(additional_list1[i][1] - additional_list2[j][1]) > minimum
                or abs(additional_list1[i][2] - additional_list2[j][2]) > minimum):
                    pass #tidak diproses
                else:
                    temp_dist = calculate_distance(additional_list1[i], additional_list2[j])
                    num_of_calc = num_of_calc + 1
                    if (temp_dist < minimum):
                        minimum = temp_dist
                        min_dist_list = []
                        min_dist_list.append([additional_list1[i], additional_list2[j]])
                    elif (temp_dist == minimum):
                        min_dist_list.append([additional_list1[i], additional_list2[j]])

    return (minimum, num_of_calc, min_dist_list)


def closest_pair_generalized(points_list, num, dimension):
    #Mencari pasangan-pasangan titik acak dalam points_list yang jaraknya terdekat
    #dengan menggunakan algoritme divide and conquer. Prasyarat: points_list harus
    #sudah dalam keadaaan terurut menaik pada absisnya, titik berdimensi dimension.
#ALGORITME
    min_dist_list = []
    if (num == 3):
        minimum, num_of_calc, min_dist_list = closest_pair_BF(points_list, num)
    elif (num == 2):
        minimum = calculate_distance(points_list[0], points_list[1])
        num_of_calc = 1
        min_dist_list.append([points_list[0], points_list[1]])
    else:
        points_list1 = []
        points_list2 = []
        
        for i in range(0, num//2, 1):
            points_list1.append(points_list[i])
        for i in range(num//2, num, 1):
            points_list2.append(points_list[i])

        minimum1, num_of_calc1, min_dist_list1 = closest_pair_generalized(points_list1, num//2, dimension)
        minimum2, num_of_calc2, min_dist_list2 = closest_pair_generalized(points_list2, num//2, dimension)
        num_of_calc = num_of_calc1 + num_of_calc2
        
        if (minimum1 < minimum2):
            minimum = minimum1
            min_dist_list = min_dist_list1
        elif (minimum2 < minimum1):
            minimum = minimum2
            min_dist_list = min_dist_list2
        else: #minimum1=minimum2
            minimum = minimum1
            min_dist_list = min_dist_list1 + min_dist_list2

        #Perhitungan dalam "STRIP"
        additional_list1 = []
        additional_list2 = []
        for point in points_list1:
            if (point[0] >= points_list[num//2 - 1][0] - minimum):
                additional_list1.append(point)
        for point in points_list2:
            if (point[0] <= points_list[num//2 - 1][0] + minimum):
                additional_list2.append(point)

        for i in range(0, len(additional_list1), 1):
            for j in range(0, len(additional_list2), 1):
                for k in range(0, dimension, 1):
                    if (abs(additional_list1[i][k] - additional_list2[j][k]) > minimum):
                        check = True
                    else:
                        check = False

                if (check == True):
                    pass #tidak diproses
                else:
                    temp_dist = calculate_distance(additional_list1[i], additional_list2[j])
                    num_of_calc = num_of_calc + 1
                    if (temp_dist < minimum):
                        minimum = temp_dist
                        min_dist_list = []
                        min_dist_list.append([additional_list1[i], additional_list2[j]])
                    elif (temp_dist == minimum):
                        min_dist_list.append([additional_list1[i], additional_list2[j]])

    return (minimum, num_of_calc, min_dist_list)


def closest_pair_BF(points_list, n):
    #Mencari pasangan-pasangan titik acak dalam points_list yang
    #jaraknya terdekat dengan menggunakan algoritme brute force
#ALGORITME
    #Inisialisasi
    min_dist_list = []
    checked = 0
    minimum = 999.0 #impossible value
    num_of_calc = 0
    
    for point in points_list:
        for i in range(checked+1, n, 1):
            distance = calculate_distance(point, points_list[i])
            num_of_calc = num_of_calc + 1
            if (distance < minimum):
                min_dist_list = []
                temp = [point, points_list[i]]
                min_dist_list.append(temp)
                minimum = distance
            elif (distance == minimum):
                temp = [point, points_list[i]]
                min_dist_list.append(temp)
                minimum = distance
        checked = checked + 1

    return(minimum, num_of_calc, min_dist_list)


def print3D(points_list, min_dist_list):
    #Mencetak titik-titik dalam bentuk gambar koordinat Cartesius
    #tiga dimensi, dengan bantuan library Matplotlib
#ALGORITME
    print("Mohon menunggu pemrosesan gambar...")
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    for point in points_list:
        x = point[0]
        y = point[1]
        z = point[2]
        ax.scatter(x,y,z, c='blue')

    for point_pair in min_dist_list:
        for point in point_pair:
            x = point[0]
            y = point[1]
            z = point[2]
            ax.scatter(x,y,z, c='red')

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.show()
