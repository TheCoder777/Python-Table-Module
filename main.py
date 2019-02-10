import csv

# ( x  /  y )
# (cols/rows)
class Table(object):
    def __init__(self, name="New Table",  col=2, row=2, content=0):
        self.name = name
        self.rows = row
        self.cols = col
        self.content = content
        self.build()

    def build(self): #'self.root' is the main table!
        self.root = [[self.content for col in range(self.cols) ]for row in range(self.rows)]
        # self.root = [[[[0,0]], [[0,0]]], [[[0,0]], [[0,0]]]] #example

    def get(self, col=None, row=None): #needs an integer, or no value at all 
        try:
            # if col > self.cols or row > self.rows:
                # print("Given col or row out of range/index!")
                # return self.root #returns the complete table if index got out of range!
            if not col and not row:
                return self.root
            elif row and not col:
                if int(row) > self.rows:
                    print("Value of given row is out of range/index!")
                    return self.root #returns the complete table if index got out of range!
                else:
                    return self.root[row]
            elif col and not row:
                if int(col) > self.cols:
                    print("Value of given row is out of range/index!")
                    return self.root #returns the complete table if index got out of range!
                else:
                    return [i[col] for i in self.root]
            else: #now col and row are given!
                if int(col) > self.cols and int(row) > self.rows:
                    print("Value of given row and col are out of range/index!")
                    return self.root #returns the complete table if index got out of range!
                else:
                    return self.root[col][row]
        except:
            print("Given col or row isn't a number!")
            return self.root #returns the complete table if an error raises!

if __name__ == "__main__":
    pass



# LICENCE

# MIT License

# Copyright (c) 2019 TheCoder777

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
