class DefaultList(list):
    def __init__(self, default):
        self.default = default

    def __getitem__(self, index):
        try:
            return list.__getitem__(self, index)
        except IndexError:
            return self.default

s = DefaultList(51)
s.extend([1, 5, 7])
indexes = [0, 2, 1000, -1]
for i in indexes:
    print(s[i], end=" ")