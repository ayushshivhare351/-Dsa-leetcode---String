s = "Welcome to the world"
arr = list(s)
# print(arr)
l = 0
r = 0
n = len(arr)

def rev(arr,i,j):
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1



while r<n:
    if arr[r] == " ":
        rev(arr,l,r-1)
        l = r+1
    r+=1
        
rev(arr,l,n-1)        

s = "".join(arr)
print(s)