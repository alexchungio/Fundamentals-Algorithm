
from Arrays.arrays import Array


class Grid(object):
    """
    two dimension array
    """
    def __init__(self, raws, cols, fill_value=None):
        self._data = Array(raws)
        for raw in range(raws):
            self._data[raw] = Array(cols, fill_value)

    def get_height(self):
        return len(self._data)

    def get_width(self):
        return len(self._data[0])

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        result = ""
        for raw in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self._data[raw][col]) + " "
            result += "\n"
        return result


if __name__ == "__main__":
    g = Grid(3, 4)
    print(g[2][0])



