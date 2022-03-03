def ordenacion(arr):
    n = len(arr)
    corte= n//2
    while corte > 0:
        for i in range(corte,n):  
            aux= arr[i]
            j = i
            while  j >= corte and arr[j-corte] >aux:
                arr[j] = arr[j-corte]
                j -= corte
  
            arr[j] = aux
        corte //= 2
arr = [ 12, 34, 54, 2, 3]
ordenacion(arr)
print(arr)