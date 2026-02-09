
# ============================
# TODO:Question 1
# ============================
def split_coords(coordinates: list) -> tuple:
    ta = [[],[]]
    if any(len(item) != 2 for item in coordinates):
        raise ValueError
    for i in coordinates:
        ta[0].append(i[0])
        ta[1].append(i[1])
    
    return tuple(ta)
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
    user_ids = list(user_ids)
    result = []
    while len(user_ids) > 0:
        if len(user_ids) > 5:
            new = user_ids[:5]
            result.append(new)
            del user_ids[:5]
        else:
            result.append(user_ids[:])
            del user_ids[:]

    return result


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
    if n < 0:
        raise ValueError
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    else:
        res = fibonacci_generator(n - 1)
        res.append(res[-1] + res[-2])
        return res




