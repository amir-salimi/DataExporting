def remove_new_line(data):
    data = data.replace("\n", "")
    data = data.replace(" ", "")
    data = data.replace("\xa0", "")
    data = data.replace("aed", "")
    data = data.replace("Sqft", "")
    return data


def delete_repeat_data(array):
    new_array = list(set(array))
    return new_array


def split_data(data_array, obj1, obj2):
    array = []
    return_array = []
    first_array = []
    second_array = []

    for data in data_array:
        for o in obj1:
            if o in data:
                first_array.append(data)
                break
            else:
                second_array.append(data)
                break

    for f in first_array:
        for o1 in obj1:
            f = f.replace(o1, "") if o1 in f else ...
        array.append(f)
    
    return_array += [array]

    if obj2 is not None:
        array = []
        for s in second_array:
            for o2 in obj2:
                if o2 in s:
                    s = s.replace(o2, "")
                    s = "0"+s if len(s) == 1 else ...
            array.append(s)
        return_array += [array]
    return return_array


