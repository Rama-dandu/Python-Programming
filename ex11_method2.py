matrix = [['😍','😍','😍'],['😍','😍','😍'],['😍','😍','😍']]
user = input("Enter the position where you want to hid the money? ")
row = int(user[0])
col = int(user[1])
matrix[row-1][col-1] = 'x';
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]} ")
