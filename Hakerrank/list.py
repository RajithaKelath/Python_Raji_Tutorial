"""The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.
"""

def insertitem(item_list , *args):
    #insert e i: Insert integer e at position 1.
    position , num = map(int , args)
    item_list.insert(position , num)
    return item_list

def removeitem(item_list , *args):
    #remove e: Delete the first occurrence of integer .
    num = map(int, args)
    item_list.remove(num)
    return item_list

def appenditem(item_list , *args):
    #append e: Insert integer  at the end of the list.
    num = int(args[0])
    item_list.append(num)
    return item_list

if __name__ == '__main__':
    N = int(input())
    current_list = []
    while N > 0:
        fun, *args = input().split()
        if fun == 'insert':
            current_list = insertitem(current_list , *args)
        elif fun == 'print':
            print(current_list)
        elif fun == 'remove':
            num = int(args[0])
            current_list.remove(num)
        elif fun == 'append':
            current_list = appenditem(current_list , *args)
        elif fun == 'sort':
            current_list.sort()
        elif fun == 'pop':
            current_list.pop()
        elif fun == 'reverse':
            current_list.reverse()
        N -= 1

