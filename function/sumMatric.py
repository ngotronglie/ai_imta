matran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def tong_ma_tran(matran):
    total = 0
    for i in range(len(matran)):
        for j in range(len(matran[i])):
            total += matran[i][j]
    return total    

print(tong_ma_tran(matran))


