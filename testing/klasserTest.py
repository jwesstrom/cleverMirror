class test(object):
    def __init__(self, bajs):
        self.bajs = bajs

    def kiss(self):
        return self.bajs + 'ah'

print test('asd').kiss()
