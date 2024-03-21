# Bubble Sort
# E S C O M
# I P N
# @autor: Diego Villagran
# @autor: Urrutia Quiroz

import random

def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):
            if A[j]<A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
    return A

def main():
    A=[random.randint(0,100) for i in range(30)]
    print("Bubble Sort")
    print("Arreglo original")
    print(A)
    BubbleSort(A)
    print("Arreglo ordenado")
    print(A)
    
main()




