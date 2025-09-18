from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()
        self.first_iteration = True

    def __next__(self):
        while True:
            item = next(self.items)

            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item

            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self

def main():
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique1 = Unique(data1)
    print(list(unique1))

    data2 = gen_random(10, 1, 3)
    unique2 = Unique(data2)
    print(list(unique2))

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique3 = Unique(data3)
    print(list(unique3))

    data4 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique4 = Unique(data4, ignore_case=True)
    print(list(unique4))  # ['a', 'b']

if __name__ == "__main__":
    main()