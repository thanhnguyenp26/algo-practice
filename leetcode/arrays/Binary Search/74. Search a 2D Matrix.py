
def searchMatrix(matrix, target) -> bool:
    i = 0
    j = len(matrix) - 1
    mid = 0
    while i <= j:
        mid = (i + j) // 2
        row = matrix[mid]
        if row[0] == target or row[-1] == target:
            return True
        elif row[0] > target:
            j = mid - 1
        elif row[-1] < target:
            i = mid + 1
        elif row[0] < target < row[-1]:
            a = 0
            b = len(row) - 1
            while a <= b:
                mid = (a + b) // 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    b = mid - 1
                else:
                    a = mid + 1
            
            return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))