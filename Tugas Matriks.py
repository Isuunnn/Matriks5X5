A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

B = [
    [15, 14, 13, 12, 11],
    [10, 9, 8, 7, 6],
    [5, 4, 3, 2, 1],
    [10, 9, 8, 7, 6],
    [5, 4, 3, 2, 1]
]

hasil = []

for i in range(5):
    baris = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil.append(baris)

for row in hasil:
    print(row)