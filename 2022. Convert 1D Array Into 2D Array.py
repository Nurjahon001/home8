def construct2DArray(original,m,n):
    if len(original) != m * n:
        return []
    result = []
    for i in range(0, len(original), n):
        result.append(original[i:i + n])
    return result

print(construct2DArray([1,2,3], 1,3))