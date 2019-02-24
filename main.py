
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
# SOFTWARE.mport csv


## Main class
# ( x  /  y )
# (cols/rows)
class Table(object):
    def __init__(self, name="New Table",  col=2, row=2, content=0, root_id=0):
        self.name = name
        self.rows = row
        self.cols = col
        self.content = content
        self.root_id = root_id
        self.head = "Name:\t\t" + str(name) + "\nDimensions:\t" + str(self.cols) + "x" + str(self.rows) #define head variable
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

    def show(self, head=True, body=True, root_id=True, brackets=True):
        if head and root_id:
            print("\n{}\nID:\t\t{}".format(self.head, self.root_id))
        elif head and not root_id:
            print("\n{}".format(self.head))
        elif root_id and not head:
            print("\nID:\t\t{}".format(self.root_id))
        else:
            pass #no head will be printed

        if body:
            print() #if head and root_id are both False, print only a newline for the body
        else:
             pass #if body is False, nothing here will be printed

        if body:
            if brackets:
                for row in self.root:
                    print(row) #print whole table with brackets and newlines
            else: #brackets is now False, or anything other we don't know
                for row in self.root:
                    print()
                    for col in row:
                        print(col, end="") #without seperators
                print()
        else: #body is now False, or anything we don't care about
            pass #body is False, so nothing here will be printed

    def sum(self, items=False, cols=False, rows=False):
        values = list()
        if items is not False:
            if isinstance(items, (list, tuple)) is list or tuple: # works with both types
                if isinstance(items[0], int) and isinstance(items[1], int): # this line is out of for loop, cause when it's in there, it would append the value two times! (cause it iterates two times over the [x,y] positions)
                    values.append(self.root[items[1]][items[0]]) # if given items only contains one position
                else:
                    for item in items: # iterate over given positions: '(col, row)'
                        values.append(self.root[item[0]][item[1]])
            else:
                print("given positions are not list neither tuple!")
                return 1 # error code system?

        if cols is not False:
            if isinstance(cols, (list, tuple)):
                for col in cols:
                    for i in self.root:
                        values.append(i[col])
            elif isinstance(cols, int):
                for i in self.root:
                    values.append(i[cols])
            else:
                print("Unvalid value for 'cols'!")

        if rows is not False:
            if isinstance(rows, (list, tuple)):
                for row in rows:
                    values.append(self.root[row])
            elif isinstance(rows, int):
                for i in self.root[rows]:
                    values.append(i)
            else:
                print("unvalid value for 'rows'!\nMust be 'lists', 'tuple' or 'int'!\nBut given value is: {}".format(type(rows)))
                    else:
                        print("Could't find any matching operator!")
                        return None
                print(values)
                return sum(values)
            # elif type(items) is tuple:
            else:
                pass
        else:
            print(type(items))

        try:
            return sum(values)
        except:
            print("could not calulate sum!")

    def __det_2x2(self, matrix):
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    def __det_3x3(self,matrix, straight=False):
        if straight:
            pass # calculate matrix directly
        else:
            first_sector = [[matrix[0][1], matrix[0][2]], [matrix[1][1], matrix[1][2]]]
            second_sector = [[matrix[0][1], matrix[0][2]], [matrix[2][1], matrix[2][2]]]
            third_sector = [[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]]
            return (matrix[0][0] * self.__det_2x2(first_sector)) - (matrix[1][0] * self.__det_2x2(second_sector)) + (matrix[2][0] * self.__det_2x2(third_sector))

    def __det_4x4(self, matrix, straight=False):
        # exaple 4x4:
        # a, b, c, d,
        # e, f, g, h,
        # i, k, l, m,
        # n, o, p, q
        first_sector = [matrix[1][1:], matrix[2][1:], matrix[3][1:]] # fgh; klm; opq
        second_sector = [matrix[0][1:], matrix[1][1:], matrix[3][1:]] # bcd; klm; opq
        third_sector = [matrix[0][1:], matrix[2][1:], matrix[3][1:]] # bcd; fgh; opq
        fourth_sector = [matrix[0][1:], matrix[1][1:], matrix[2][1:]] # bcd; fgh; klm
        return (matrix[0][0] * self.__det_3x3(first_sector)) - (matrix[1][0] * self.__det_3x3(second_sector)) + (matrix[2][0] * self.__det_3x3(third_sector)) - (matrix[0][3] * self.__det_3x3(fourth_sector))

    def det(self, straight=False): # add 'straight' mode later (calculate 3x3 directly, not using 2x2)
        if self.cols == self.rows:
            if self.cols and self.rows == 2:
                return self.__det_2x2(self.root)
            elif self.cols and self.rows == 3:
                if straight:
                    pass
                else:
                    return self.__det_3x3(self.root)
            elif self.cols and self.rows == 4:
                return self.__det_4x4(self.root)
            else:
                print("matrix is to big to calculate!")
                return None

if __name__ == "__main__":
    pass

