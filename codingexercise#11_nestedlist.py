#WAP take 3x3 matrix as with 1 as all elements.
# take input from user which element he wants to block in matrix example 32 means 3 rd row x 2 coloumn element he want to block like that.
# from nestedlist import numbers
#method1
input_matrix = [[1,1,1],[1,1,1],[1,1,1]]
user = input("Enter which element you want to block? ")
# print(user)
num = int(user)
# print(num)
row = int(num/10);
col = num%10;
# print(row)
# print(col)
input_matrix[row-1][col-1] = 'x';
print(f"{input_matrix[0]}\n{input_matrix[1]}\n{input_matrix[2]} ")
