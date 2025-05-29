def subarraySum(numRows):
    result = [[1]]
    col = 0
    for row in range(1,numRows):
        pascal_row = [1]
        for col in range(1,row):
            ans = pascal_row[-1] * row // col
            pascal_row+=[ans]
        pascal_row+=[1]
        result+=[pascal_row]
    return result
print(subarraySum(5))