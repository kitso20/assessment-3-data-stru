def batch_api_dispatcher(user_ids: list | tuple) -> list:
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

print(batch_api_dispatcher(['A', 'B', 'C', 'D', 'E', 'F']))