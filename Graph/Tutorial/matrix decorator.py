def grid_decorator(mat):

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j == len(mat[0]) - 1:
                if i == len(mat) - 1:
                    print(f"{mat[i][j]}]", end="")
                else:
                    print(f"{mat[i][j]}]", end=",")
            elif j == 0:
                print(f"[{mat[i][j]}", end=", ")
            else:
                print(mat[i][j], end=", ")
        print()

grid = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]

grid_decorator(grid)
