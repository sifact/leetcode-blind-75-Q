# def flood_fill(image, sr, sc, new_color):
#     pass
#
#     def dfs(i, j):
#         image[i][j] = new_color
#
#         for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
#             if 0 <= x < r and 0 <= y < c and old == image[x][y]:
#                 dfs(x, y)
#
#     old, r, c = image[sr][sc], len(image), len(image[0])
#     if old != new_color:
#         dfs(sr, sc)
#
#     return image
#
#
# matrix = [
#     [0, 0, 0],
#     [0, 1, 0]
# ]
#
#
# print(flood_fill(matrix, 1, 0, 2))


# def number_of_island(matrix1):
#     pass
#
#     def dfs(i, j, add, mx):
#         pass
#         matrix1[i][j] = 2
#
#         for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
#             if 0 <= x < r and 0 <= y < c and matrix1[x][y] == "1":
#
#                 dfs(x, y, add, mx)
#                 add += 1
#                 mx = max(mx, add)
#         print(mx)
#
#     r, c = len(matrix1), len(matrix1[0])
#     count = 0
#
#     for i in range(r):
#         for j in range(c):
#             if matrix1[i][j] == "1":
#
#                 count += 1
#
#                 dfs(i, j, 1, 0)
#
#
#
# mat = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]

# print(number_of_island(mat))


# def max_area_of_island(grid):
#     pass
#
#     r, c = len(grid), len(grid[0])
#
#     def dfs(i, j):
#         pass
#
#         if 0 <= i < r and 0 <= j < c and grid[i][j] == "1":
#             grid[i][j] = 0
#             up = dfs(i + 1, j)
#             bottom = dfs(i - 1, j)
#             right = dfs(i, j + 1)
#             left = dfs(i, j - 1)
#
#             return up + bottom + right + left + 1
#         return 0
#
#     count = 0
#     for i in range(r):
#         for j in range(c):
#             if grid[i][j]:
#                 count = max(dfs(i, j), count)
#
#     return count
#
#
# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]

# print(max_area_of_island(grid))


# class Solution:
    # def closed_island(self, grid):
    #     # 0's are island
    #
    #     def dfs(x, y):
    #         if x in (0, r - 1) or y in (0, c - 1):
    #             self.is_island = False
    #
    #         for i, j in ((x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)):
    #             if 0 <= i < r and 0 <= j < c and grid[i][j] == 0:
    #                 grid[i][j] = -1
    #                 dfs(i, j)
    #
    #
    #     r, c, count = len(grid), len(grid[0]), 0
    #
    #     for i in range(r):
    #         for j in range(c):
    #             if grid[i][j] == 0:
    #                 self.is_island = True
    #                 dfs(i, j)
    #                 count += self.is_island
    #     return count
#     def closed_island(self, grid):
#         def dfs(i, j):
#             if 0 <= i < r and 0 <= j < c and grid[i][j] == 0:
#                 if i in (0, r - 1) or j in (0, c - 1):
#                     self.is_island = False
#                 grid[i][j] = -1
#                 dfs(i - 1, j)
#                 dfs(i + 1, j)
#                 dfs(i, j - 1)
#                 dfs(i, j + 1)
#
#         r, c, count = len(grid), len(grid[0]), 0
#
#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j] == 0:
#                     self.is_island = True
#                     dfs(i, j)
#                     count += self.is_island
#         return count
#
#
# mat = [[0,0,1,0,0],
#        [0,1,0,1,0],
#        [0,1,1,1,0]]
# grid = Solution()
# print(grid.closed_island(mat))


class Solution1(object):
    def num_enclaves(self, grid):

        def dfs(i, j):
            if 0 <= i < r and 0 <= j < c and grid[i][j] == 1:
                if i in (0, r - 1) or j in (0, c - 1):
                    self.is_island = False

                grid[i][j] = -1

                up = dfs(i - 1, j)
                down = dfs(i + 1, j)
                left = dfs(i, j - 1)
                right = dfs(i, j + 1)
                return 1 + up + down + left + right

            return 0

        r, c, count = len(grid), len(grid[0]), 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    self.is_island = True
                    island = dfs(i, j)
                    if self.is_island:
                        count += island
        return count


mat = [[0,1, 0,0],
       [0,0,1,0],
       [0,0,1,0],
       [0,0,0,0]]
g = Solution1()
# print(g.num_enclaves(mat))


def count_sub_island(grid1, grid2):
    pass
    count, r, c = 0, len(mat2), len(mat2[0])

    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c or grid2[i][j] == 0:
            return

        grid2[i][j] = 0
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
        dfs(i - 1, j)

    for i in range(r):
        for j in range(c):
            if grid2[i][j] == 1 and grid1[i][j] == 0:
                dfs(i, j)

    # for i in range(r):
    #     for j in range(c):
    #         if mat2[i][j] == 1:
    #             dfs(i, j)
    #             count += 1
    # return count
    return grid2

mat1 = [
    [1,0,1,0,1],
     [1,1,1,1,1],
     [0,0,0,0,0],
     [1,1,1,1,1],
     [1,0,1,0,1]
]
mat2 = [
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [1,0,0,0,1]

]


# print(count_sub_island(mat1, mat2))

from collections import deque


def max_distance(grid):
    m, n = len(grid), len(grid[0])
    
    q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])

    if len(q) == m * n or len(q) == 0:
        return -1
    level = 0
    while q:
        size = len(q)
        for _ in range(size):
            i, j = q.popleft()
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = x + 1, y + j
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    q.append((x, y))
                    grid[x][y] = 1

        level += 1

    return level - 1

mat = [
    [1,0,0],
    [0,0,0],
    [0,0,0]
]
print(max_distance(mat))
