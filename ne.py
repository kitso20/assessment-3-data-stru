def split_coords(coordinates: list) -> tuple:
    ta = [[],[]]
    for i in coordinates:
        ta[0].append(i[0])
        ta[1].append(i[1])
        if len(ta[0]) == len(ta[1]):
    return tuple(ta)

print(split_coords([(12, 45), (15, 48), (18, 51)]))