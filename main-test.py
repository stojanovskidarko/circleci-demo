from main import Add

def testAdd():
    assert Add(2,3) == 5
    assert Add(5,5) == 10
    print('Add Function works correctly')

if __name__ == '__main__':
        testAdd()