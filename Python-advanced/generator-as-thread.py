from collections import deque

friends = deque(('Rolf','Anna','Bob','Charlie','Jose'))

def get_friend():
    yield from friends

c = get_friend()
while True:
    try:
        print(next(c))
    except StopIteration:
        print("Iteration stopped")
        break
