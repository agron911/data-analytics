numRows = 5

def pascal(numRows):
    if not numRows:
        return 0
    triangle = [[0 for j in range(i+1)] for i in range(numRows)]
    triangle[0] =[1]

    for i in range(1,numRows):
        row = []
        for j in range(i+1):
            num = 0
            if i>j:
                num = triangle[i-1][j]
            if i>j-1>=0:
                num += triangle[i-1][j-1]
            row.append(num)
        triangle[i]=row
    return triangle
print(pascal(numRows))