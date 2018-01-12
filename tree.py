tree = \
{'Bath': ['Clothes'],
 'Brush Teeth': ['Have Breakfast'],
 'Clothes': [],
 'Exercise': ['Bath'],
 'Get Up': ['Exercise', 'Brush Teeth', 'Package Lunch'],
 'Have Breakfast': [],
 'Package Lunch': []}

"""
Get Up --> Exercise --> Bath --> Clothes
      \--> Brush Teeth --> Have Breakfast
      \--> Package Lunch
"""

# 这个方法可以交互式体验完成tree中的工作
def Do_work(name):
    current_cando = []
    already_done = []
    already_done.append(name)
    current_cando += tree[name]
    while current_cando:
        print('='*40)
        print("What can do now is: \n" + str(current_cando))
        work = input('Do a work: ')
        if work in tree:
            already_done.append(work)
            current_cando.remove(work)
            current_cando += tree[work]
        else:
            print("You can't do that, input again!")
            continue
    print("All done: ")
    print(already_done)
Do_work('Get Up')

# 这个方法自动列出所有可能的工作路径
def AutoDoWork(can_do):
    if len(can_do) == 0:
        yield []
    else:
        for i in can_do:
            next_can_do = [w for w in can_do if w!=i]
            next_can_do.extend(tree[i])
            for j in AutoDoWork(next_can_do):
                yield [i] + j
#list(AutoDoWork(tree['Bath']))
#list(AutoDoWork(tree['Exercise']))
print(len(list(AutoDoWork(tree['Get Up'])))



