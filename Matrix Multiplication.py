rows = int(input("Enter rows of first matrix: "))
cols = int(input("Enter columns of first matrix: "))

print("Enter first matrix:")
a = [list(map(int, input().split())) for _ in range(rows)]

print("Enter second matrix:")
b = [list(map(int, input().split())) for _ in range(cols)]

result = [[0 for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        for k in range(cols):
            result[i][j] += a[i][k] * b[k][j]

print("Multiplication Result:")

for row in result:
    print(*row)