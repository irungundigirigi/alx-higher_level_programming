def pascal_triangle(n):
    """Generate Pascal's Triangle with 'n' rows"""
    if n <= 0:
        return []

    triangle = [[1]]
    
    while len(triangle) != n:
        previous_row = triangle[-1]
        new_row = [1]
        
        for i in range(len(previous_row) - 1):
            new_element = previous_row[i] + previous_row[i + 1]
            new_row.append(new_element)
        
        new_row.append(1)
        triangle.append(new_row)
    
    return triangle

