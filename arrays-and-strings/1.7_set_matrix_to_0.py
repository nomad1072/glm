import numpy

input_list_matrices = [
    [
        [ 1,  2,  3,  4,  5   ],
        [ 6,  7,  8,  9,  10  ],
        [ 11, 12, 13, 14, 0   ],
        [ 15, 16, 17, 18, 19  ]
    ],
    [
        [ 0,  2,  3,   4,  5  ],
        [ 6,  7,  0,   9,  10 ],
        [ 11, 12, 13,  14, 0  ],
        [ 15, 16, 0,   18, 0  ]
    ],
    [
        [ 1,  2,  3,  4,  5   ],
        [ 6,  7,  8,  9,  10  ],
        [ 11, 12, 13, 14, 0   ],
        [ 15, 16, 17, 18, 19  ]
    ]
]

for index, p in enumerate(input_list_matrices):
    print('Input Matrix: ', p)
    row = [False] * len(p)
    columns = [False] * len(p[0])

    for index in range(len(p)):
        for indexj in range(len(p[0])):
            if p[index][indexj] == 0:
                row[index] = True
                columns[indexj] = True

    for index in range(len(p)):
        for indexj in range(len(p[0])):
            if row[index] or columns[indexj]:
                p[index][indexj] = 0

    print('Output Matrix: ', p)