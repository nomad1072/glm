n = int(input('Enter the number of steps: '))

ways = [0] * n
ways[0] = 1
ways[1] = 2
print('Ways: ', ways)
for i in range(2, n):
    ways[i] = ways[i-1] + ways[i-2]

print('Number of ways to reach %d-th step is: %d' % (n, ways[n-1]))