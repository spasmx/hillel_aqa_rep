# Write a ReverseIterator that takes a list of any objects and iterates over them in reverse order.
# It needs to be implemented as a class.

class ReverseIterator:
    def __init__(self, data_list: list):
        self.data_list = data_list
        self._index = 0

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> str:
        if len(self.data_list) == 0:
            return 'Empty'
        if len(self.data_list) == 1:
            return self.data_list[0]
        if self._index < len(self.data_list):
            reversed_data_list = self.data_list[::-1]
            elem = reversed_data_list[self._index]

            self._index += 1

            return elem

        raise StopIteration







