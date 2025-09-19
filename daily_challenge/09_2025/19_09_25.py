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

# Unit tests
import unittest

class TestSpreadsheet(unittest.TestCase):

    def test_case_1(self):
        spreadsheet = Spreadsheet(3)
        spreadsheet.setCell("A1", 5)
        spreadsheet.setCell("B2", 3)
        self.assertEqual(spreadsheet.getValue("=A1+B2"), 8)
        spreadsheet.resetCell("A1")
        self.assertEqual(spreadsheet.getValue("=A1+B2"), 3)
        self.assertEqual(spreadsheet.getValue("=A1+10"), 10)
        self.assertEqual(spreadsheet.getValue("=10+20"), 30)

    def test_case_2(self):
        spreadsheet = Spreadsheet(5)
        spreadsheet.setCell("C3", 7)
        self.assertEqual(spreadsheet.getValue("=C3+0"), 7)
        spreadsheet.resetCell("C3")
        self.assertEqual(spreadsheet.getValue("=C3+0"), 0)
        self.assertEqual(spreadsheet.getValue("=0+0"), 0)

if __name__ == "__main__":
    unittest.main()