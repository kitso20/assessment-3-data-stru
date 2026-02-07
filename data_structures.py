
# ============================
# TODO:Question 1
# ============================
def split_coords(coordinates: list) -> tuple:
    ta = [[],[]]
    for i in coordinates:
        ta[0].append(i[0])
        ta[1].append(i[1])
    if len([0]) == len(ta[1]):
        return tuple(ta)
    else:
        raise ValueError


# ============================
# TODO:Question 2
# ============================
def create_id_lookup(user_data: list) -> dict:
    
    return {k:v for v,k in enumerate(user_data)}


# ============================
# TODO:Question 3
# ============================
def extract_unique_tags(posts: list) -> set:
    
    return {item.lower() for item in posts}


# ============================
# TODO:Question 4
# ============================
def group_by_category(items: list) -> dict:
    new = {}
    for item in items:
        key = item['type']
        value = item['name']
        if key in new:
            new[key].append(value)
        else:
            new[key] = [value]
    return new


# ============================
# TODO:Question 5
# ============================
def batch_api_dispatcher(user_ids: list | tuple) -> list:
    new = []
    into = []
    while len(into) != 5:
        fir = user_ids.pop(0)
        into.append(fir)
    
    
        return []


# ============================
# TODO:Question 6
# ============================
def social_graph_inverter(following_list: dict) -> dict:
    
    ew = {}
    for k,v in following_list.items():
        for n in v:
            if n not in ew:
                ew[n] = []
            ew[n].append(k)

    return ew


# ============================
# TODO:Question 7
# ============================
def fibonacci_generator(n: int) -> list:
    lst = [0,1]
    if len(lst) == n:
        return lst
    else:
        lst.append(fibonacci_generator(lst[-1]+lst))




