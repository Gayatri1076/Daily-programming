rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

print("Enter first matrix:")
a = [list(map(int, input().split())) for _ in range(rows)]

print("Enter second matrix:")
b = [list(map(int, input().split())) for _ in range(rows)]

result = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(a[i][j] + b[i][j])
    result.append(row)

print("Result:")

for row in result:
    print(*row)