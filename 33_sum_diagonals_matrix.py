"Write a Program to showSum of Diagonals (major and minor) in Two Dimensional List"

MATRIX = []

def create_matrix():
    global MATRIX
    row_n = int(input("Enter Dimension (Square Matrix Only):"))
    for i in range(row_n):
        MATRIX.append([]) # add new row
        for j in range(row_n):
            MATRIX[i].append(int(input(f"Enter Value for ROW {i} COL {j}: ")))
    
    # print the matrix
    for row in MATRIX:
        print(row)

def calc_diagonals():
    global MATRIX
    primary_diag = 0
    secondary_diag = 0
    _len = len(MATRIX)
    for i in range(_len):
        primary_diag += MATRIX[i][i]
        secondary_diag += MATRIX[i][_len - i - 1]
        
    return primary_diag, secondary_diag

def main():
    create_matrix()
    diag_p, diag_s = calc_diagonals()
    print(f"Primary Diagonal: {diag_p} \nSecondary Diagonal: {diag_s}")


if __name__ == "__main__":
    main()

