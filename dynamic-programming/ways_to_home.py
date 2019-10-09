import numpy as np
rows = int(input('Enter the rows in the grid: '))
columns = int(input('Enter the columns in the grid: '))

# ways = [[0]*(columns+1)]*(rows+1)
# ways[1:] = [1]*(columns)
# ways[:1] = [1]*(rows)
ways = np.zeros(shape=(rows+1,columns+1))
ways[1,:] = [0] + [1] * columns
ways[:,1] = [0] + [1] * rows

print('Ways: ', ways)

for i in range(2, rows+1):
    for j in range(2, columns+1):
        ways[i][j] = ways[i-1][j] + ways[i][j-1]

print('Ways: ', ways)
print('Ways to reach home is: %d' % ways[rows][columns])

