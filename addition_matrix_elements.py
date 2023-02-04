matrix = []
while True:
    a = str(input())
    if a == 'end':
        break
    else:
        matrix.append(a.split())

length = len(matrix[0])
high = len(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        c = int(matrix[(i-1) % high][j]) + int(matrix[(i+1) % high][j]) \
            + int(matrix[i][(j-1) % length]) + int(matrix[i][(j+1) % length])
        print(c, end=" ")
    print()