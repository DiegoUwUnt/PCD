# Quick Sort
# E S C O M
# I P N
# @autor: Diego Villagran
# @autor: Urrutia Quiroz
import random


def Partition (A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
            if A[j]<=x:
                i+=1
                A[i],A[j]=A[j],A[i]
                
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def QuickSort(A,p,r):
    if p<r:
        q=Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)
    return A


def main():
    A=[random.randint(0,100) for i in range(30)]
    print("Quick Sort")
    print("Arreglo original")
    print(A)
    QuickSort(A,0,len(A)-1)
    print("Arreglo ordenado")
    print(A)
    
main()