def nameSorter(badNames): 
  size =  len(badNames)
  for i in range(size):
        for j in range(0, size-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
name = 'ALICE'
name = name.upper()
arr = list(name)
nameSorter(arr)
str1 = ''.join(arr)
print (str1)
