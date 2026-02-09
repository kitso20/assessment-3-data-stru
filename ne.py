def batch_api_dispatcher(user_ids: list | tuple) -> list:
    # res = []
    # user_ids = list(user_ids)
    # while len(user_ids) > 0:
    #     for i in range(5):
    #         user_ids.pop()
    res = []
    while len(user_ids) > 0:
        pop_item = user_ids[:5]
        res.append(pop_item)
        del user_ids[:5]
    return res
    # return [user_ids[i:i+5] for i in range(0,len(user_ids),5)]
print(batch_api_dispatcher(['A', 'B', 'C', 'D', 'E', 'F']))