n = 7

pascal = []

for i in range(n + 1):
     row = []

     for j in range(1 + i):
          if j == 0 or j == i:
               row.append(1)
          else:
               row.append(pascal[i-1][j-1] + pascal[i-1][j])

     pascal.append((row))

for row in pascal:
     print(*row)