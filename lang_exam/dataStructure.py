def dicts_test():
    player = {'name': 'kim', 'age': 12, 'win': 10, 'sub': []}
    print(player.get('name'))
    print(player.get('win'))

    player.pop('age') # 삭제
    print(player)
    player['sub'].append('test')
    print(player.get('sub'))

def tuple_test():  # 튜블은 불변
    tuple = ("a", "b", "c")
    print(tuple[0])

def list_test():
    list = [0,1,2]
    a, b ,c= list
    print(a, b, c)


if __name__ == '__main__':
    # tupleTest()
    # dicts_test()
    list_test()
