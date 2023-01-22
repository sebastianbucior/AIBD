from typing import List


def bubble_sort(data: List[int], ite_: bool = False):
    if not isinstance(data, List) or not all(isinstance(x, int) for x in data):
        return None
    else:
        if ite_:
            ite: int = 0
        for i in range(len(data) - 1):
            sth_changed: bool = False
            if ite_:
                ite += 1
            for j in range(len(data) - 1 - i):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    sth_changed = True
            if not sth_changed:
                if ite_:
                    return data, ite
                else:
                    return data

        if ite_:
            return data, ite
        else:
            return data
