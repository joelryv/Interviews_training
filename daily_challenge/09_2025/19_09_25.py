"""
https://leetcode.com/problems/design-spreadsheet/description/?envType=daily-question&envId=2025-09-19
"""

class Spreadsheet:

    def __init__(self, rows: int):
        self.data = {}

    def setCell(self, cell: str, value: int) -> None:
        self.data[cell] = value

    def resetCell(self, cell: str) -> None:
        self.data[cell] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+')
        result = 0
        if a in self.data.keys():
            result += self.data[a]
        elif a.isdigit():
            result += int(a)
        else:
            result += 0
        if b in self.data.keys():
            result += self.data[b]
        elif b.isdigit():
            result += int(b)
        else:
            result += 0
        return result

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)