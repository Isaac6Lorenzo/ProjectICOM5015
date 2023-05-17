import time as t
import random as rd
import numpy as np
import matplotlib.pyplot as plot
import csv




# ITERATIVE PYTHON CODE

def create_1D_array(arraySize, int_random):

    arr = []

    for i in range(arraySize):

        arr.append(rd.randint(0, int_random))

    return arr



def create_2D_array(row, col, int_random):

    arrarSize = col

    arr = []

    for x in range(row):

        new_arr = create_1D_array(arrarSize, int_random)

        if x == 0:

            arr = [new_arr]

        else:

            arr = arr + [new_arr]

    return arr



def product_1D_array(arrayA, arrayB):

    sum = 0

    for i in range(len(arrayA)):

        for j in range(len(arrayB)):

            if i == j:

                product = arrayA[i] * arrayB[j]

                sum = sum + product

    return sum



def product_2D_array(arrayA, arrayB):

    arrayC = []

    if len(arrayB) != len(arrayA[0]):

        print("No se puede multiplicar las dos matrices "

              "debido a que no son compatibles \npor no "

              "tienen el mismo numero de fila de la matriz A "

              "que el mismo \nnumero de columnas de la matri B.")

        print("Se devuelve una matriz vacia.")

        return arrayC



    else:

        arrayC = create_2D_array(len(arrayA), len(arrayB[0]), 0)

        # num de filas A

        for i in range(len(arrayA)):

            # num de col B

            for j in range(len(arrayB[0])):

                sum = 0

                # num de col A

                for k in range(len(arrayA[0])):

                    sum = sum + arrayA[i][k] * arrayB[k][j]



                arrayC[i][j] = sum



        return arrayC





# NUMPY CODE

## CREATE A 1-D ARRAY OF RANDOM INTEGERS

def create_1D_array_numpy(sizeArray):

    return np.random.randint(1, 1000001, sizeArray)



## CREATE A  2-D ARRAY OF RANDOM INTEGERS

def create_2D_array_numpy(row, col):

    return np.random.randint(1, 1000001, size=(row, col))



## GET PRODUCT NUMPY

def product_ND_array_numpy(arrayA, arrayB):

    return np.dot(arrayA, arrayB)



# EXPORT CODE TO CSV

def create_1D_list(sizeList, sizeArray):

    arrayA = create_1D_array(sizeList, 0)

    for i in range(len(arrayA)):

        arrayB = create_1D_array(sizeArray, 256)

        arrayA[i] = arrayB

    return arrayA



def create_2D_list(sizeList, sizeArray):

    arrayA = create_1D_array(sizeList, 0)

    for i in range(len(arrayA)):

        arrayB = create_2D_array(sizeArray, sizeArray, 256)

        arrayA[i] = arrayB

    return arrayA



def create_1D_list_numpy(sizeList, sizeArray):

    arrayA = create_1D_array(sizeList, 0)

    for i in range(len(arrayA)):

        arrayB = create_1D_array_numpy(sizeArray)

        arrayA[i] = arrayB

    return arrayA



def create_2D_list_numpy(sizeList, sizeArray):

    arrayA = create_1D_array(sizeList, 0)

    for i in range(len(arrayA)):

        arrayB = create_2D_array_numpy(sizeArray, sizeArray)

        arrayA[i] = arrayB

    return arrayA



# Writer method CSV File

def writerCVS_1D(title, sizeList, sizeArray, inc):

    csv_file = title + ".csv"

    field = ['sizeArray', 'time_execution_s']



    with open(csv_file, mode="w", newline='') as file:

        writer = csv.writer(file)

        writer.writerow(field)

        for x in range(1, (inc+1)):

            newsize = sizeArray * x

            arrayA = create_1D_list(sizeList, newsize)

            arrayB = create_1D_list(sizeList, newsize)



            for i in range(len(arrayA)):

                begin = t.time_ns()

                product = product_1D_array(arrayA[i], arrayB[i])

                end = t.time_ns()

                t_exec = (end - begin) * 10**-9

                print("1D product size:", newsize, "seconds: ", t_exec)

                writer.writerow([newsize, t_exec])



        file.close()

    return 0



def writerCVS_2D(title, sizeList, sizeArray, inc):

    csv_file = title + ".csv"

    field = ['sizeArray', 'time_execution_s']

    product = create_1D_array(sizeList, 0)



    with open(csv_file, mode="w", newline='') as file:

        writer = csv.writer(file)

        writer.writerow(field)



        for x in range(1, (inc+1)):

            newsize = sizeArray * x

            arrayA = create_2D_list(sizeList, newsize)

            arrayB = create_2D_list(sizeList, newsize)

            for i in range(len(arrayA)):

                begin = t.time_ns()

                product[i] = product_2D_array(arrayA[i], arrayB[i])

                end = t.time_ns()

                t_exec = (end - begin) * 10**-9

                print("2D product size:", newsize, "seconds: ", t_exec)

                writer.writerow([newsize, t_exec])



        file.close()



    return 0



def writerCVS_1D_numpy(title, sizeList, sizeArray, inc):

    csv_file = title + ".csv"

    field = ['sizeArray', 'time_execution_s']



    with open(csv_file, mode="w", newline='') as file:

        writer = csv.writer(file)

        writer.writerow(field)

        for x in range(1, (inc+1)):

            newsize = sizeArray * x

            arrayA = create_1D_list_numpy(sizeList, newsize)

            arrayB = create_1D_list_numpy(sizeList, newsize)



            for i in range(len(arrayA)):

                begin = t.time_ns()

                product = product_ND_array_numpy(arrayA[i], arrayB[i])

                end = t.time_ns()

                t_exec = (end - begin) * 10**-9

                print("1D product numpy size:", newsize, "seconds: ", t_exec)

                writer.writerow([newsize, t_exec])



        file.close()

    return 0



def writerCVS_2D_numpy(title, sizeList, sizeArray, inc):

    csv_file = title + ".csv"

    field = ['sizeArray', 'time_execution_s']



    with open(csv_file, mode="w", newline='') as file:

        writer = csv.writer(file)

        writer.writerow(field)

        for x in range(1, (inc + 1)):

            newsize = sizeArray * x

            arrayA = create_2D_list_numpy(sizeList, newsize)

            arrayB = create_2D_list_numpy(sizeList, newsize)



            for i in range(len(arrayA)):

                begin = t.time_ns()

                product = product_ND_array_numpy(arrayA[i], arrayB[i])

                end = t.time_ns()

                t_exec = (end - begin) * 10**-9

                print("2D product numpy size:", newsize, "seconds: ", t_exec)

                writer.writerow([newsize, t_exec])



        file.close()

    return 0



# main

if __name__ == '__main__':



    # This section of code was designed to store multiple files with the time it took to

    # compute the product of arrays of dimensions as big as 1000000000. Because of technical

    # limitations -that did not seem obvious at the beginning of the project- it was not fully

    # utilized. However, we felt it necessary to keep it as a testament of our blissfull ignorance.



    print("Iteration product 1D")

    writerCVS_1D("1DM10_1000", 1, 10, 50)

    # writerCVS_1D("1DM1000_100000", 10, 1000, 10)

    # writerCVS_1D("1DM100000_10000000", 10, 100000, 100)

    # writerCVS_1D("1DM10000000_1000000000", 10, 10000000, 100)

    print("---------------------------------------------------")

    # print("Iteration product 2D")

    writerCVS_2D("2DM10_1000", 1, 10, 50)

    # writerCVS_2D("2DM1000_10000", 10, 1000, 10)

    # writerCVS_2D("2DM100000_10000000", 10, 100000, 100)

    # writerCVS_2D("2DM10000000_1000000000", 10, 10000000, 100)

    #

    print("---------------------------------------------------")

    print("---------------------------------------------------")

    #

    # print("Numpy product 1D")

    writerCVS_1D_numpy("1DN10_1000", 1, 10, 50)

    # writerCVS_1D_numpy("1DN1000_100000", 10, 1000, 100)

    # writerCVS_1D_numpy("1DN100000_10000000", 10, 100000, 100)

    # writerCVS_1D_numpy("1DN10000000_1000000000", 10, 10000000, 100)

    print("---------------------------------------------------")

    # print("Numpy product 2D")

    writerCVS_2D_numpy("2DN10_1000", 1, 10, 50)

    # writerCVS_2D_numpy("2DN1000_100000", 10, 1000, 100)

    # writerCVS_2D_numpy("2DN100000_10000000", 10, 100000, 100)

    # writerCVS_2D_numpy("2DN10000000_1000000000", 10, 10000000, 100)



