list_number = [x for x in range(13)]

n = int(input("items per chunk: "))
index_end = int(n)

index_start = 0


while True:
    row_item = list_number[index_start:index_end]
    if len(row_item) > 0 :
        print(row_item)
        index_start += n
        index_end += n
    else:
        break
