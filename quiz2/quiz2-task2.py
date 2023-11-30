class MyMatrix:
    def __init__(self, rows, columns):
        self.row_size = rows
        self.column_size = columns
        self.values = [0 for _ in range(rows*columns)] # initialize with 0s, though not specified

    # calculates offset in th elist
    def __offset(self, x,y):
        return y * self.row_size + x

    def set(self, x, y, new_val):
        self.values[self.__offset(x, y)] = new_val
    
    def get(self, x, y):
        return self.values[self.__offset(x, y)]
    
    def total_sum(self):
        return sum(self.values)

    def primary_diagonal_sum(self):
        # diagonals can only be defined in n*n matrix
        if self.column_size != self.row_size:
            return None
        
        return sum([self.values[i] for i in range(0, len(self.values), self.row_size+1)])

    def secondary_diagonal_sum(self):
        # diagonals can only be defined in n*n matrix
        if self.column_size != self.row_size:
            return None

        return sum([self.values[i] for i in range(self.row_size-1, len(self.values)-1, self.row_size-1)])


    def __str__(self):
        res = []
        for i in range(self.row_size):
            res.append(self.values[i*self.row_size:i*self.row_size+self.column_size])
        return "\n".join([" ".join([str(col) for col in row ]) for row in res])

        
if __name__ == "__main__":
    # Test case 1
    n = 3
    m = MyMatrix(n, n)

    for i in range(n):
        for j in range(n):
            m.set(i, j, j*n+i)

    print("The matrix:", m, sep="\n")
    print("Total sum:", m.total_sum())
    print("Primary diagonal:", m.primary_diagonal_sum())
    print("Secondary diagonal:", m.secondary_diagonal_sum())

    # Test case 2
    import random
    n = 4
    m = MyMatrix(n, n)

    for i in range(n):
        for j in range(n):
            m.set(i, j, random.randint(0,9))

    print("The matrix:", m, sep="\n")
    print("Total sum:", m.total_sum())
    print("Primary diagonal:", m.primary_diagonal_sum())
    print("Secondary diagonal:", m.secondary_diagonal_sum())

    # Test case 3
    import random
    m = MyMatrix(4, 6)

    for i in range(n):
        for j in range(n):
            m.set(i, j, random.randint(0,9))

    print("The matrix:", m, sep="\n")
    print("Total sum:", m.total_sum())
    print("Primary diagonal:", m.primary_diagonal_sum())
    print("Secondary diagonal:", m.secondary_diagonal_sum())

    # Test case 4
    import random
    n = 20
    m = MyMatrix(n, n)


    for i in range(n):
        for j in range(n):
            m.set(i, j, random.randint(0,9))

    print("The matrix:", m, sep="\n")
    print("Total sum:", m.total_sum())
    print("Primary diagonal:", m.primary_diagonal_sum())
    print("Secondary diagonal:", m.secondary_diagonal_sum())
