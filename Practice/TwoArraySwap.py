A = [4,2,1,5,3]
B = [1,5,4,6,5]
N = 5
K = 3

for i in range(N):
    min_index = i
    for j in range(i+1,N):
        if A[i] > A[j] :
            min_index = j
    A[i], A[min_index] = A[min_index],A[i]
        
for i in range(N):
    min_index = i
    for j in range(i+1,N):
        if B[i] > B[j] :
            min_index = j
    B[i], B[min_index] = B[min_index],B[i]

print(A)
print(B)

for i in range(0,K,1):
    if A[i] < B[N-1-i] :
        A[i],B[N-1-i] = B[N-1-i],A[i]
    else:
        break


print(A)
print(B)

print(sum(A))