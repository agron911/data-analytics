numRows = 5

def pascal(numRows):
    if not numRows:
        return 0
    triangle = [[0 for j in range(i)]]