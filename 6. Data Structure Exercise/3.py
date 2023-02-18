def make_3_slices(list):
    start = 0
    end = len(list) // 3
    for i in range(3):
        ind = slice(start, end)
        chunk = list[ind]
        print(f'Chunk {i + 1}: {chunk}')
        start = end
        end += len(list) // 3
    return ''


list1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print(make_3_slices(list1))