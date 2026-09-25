class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        def flatten(nested):
            for item in nested:
                if item.isInteger():
                    yield item.getInteger()
                else:
                    yield from flatten(item.getList())

        self.generator = flatten(nestedList)
        self.next_value = None

    def next(self) -> int:
        if self.next_value is not None:
            value = self.next_value
            self.next_value = None
            return value

        return next(self.generator)

    def hasNext(self) -> bool:
        if self.next_value is not None:
            return True

        try:
            self.next_value = next(self.generator)
            return True
        except StopIteration:
            return False