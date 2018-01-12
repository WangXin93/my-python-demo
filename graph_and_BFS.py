graph = \
{'alice': ['peggy'],
 'anuj': [],
 'bob': ['anuj', 'peggy'],
 'claire': ['thom', 'jonny'],
 'jonny': [],
 'peggy': [],
 'thom': [],
 'you': ['alice', 'bob', 'claire']}

"""
anuj <-- bob <-- you --> claire --> thom
          |       |         \
          v       v          \-->jonny
         peggy <-- alice
"""

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
