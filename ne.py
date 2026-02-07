def split_coords(coordinates: list) -> tuple:
    ta = [[],[]]
    if any(len(item) != 2 for item in coordinates):
        raise ValueError
    for i in coordinates:
        ta[0].append(i[0])
        ta[1].append(i[1])
    
    return tuple(ta)
print(split_coords([(1, 2), (3, 4), (5, 6)]))