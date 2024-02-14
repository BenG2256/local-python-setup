def max_num(x, y, z):
    return max([x,y,z])

print(max_num(150,200,57))

def mult_list(params):
    
    if len(params) == 0:
        return 0
    prod = params[0]
    
    if len(params) > 1:
        for i in params[1:]:
            prod = prod * i
            
    return prod

print(mult_list([2, 3, 6]))


def rev_string(str):
    return str[::-1]

print(rev_string("tacotruck"))

def num_within(a,b,c):
    return a in range(b,c+1)

print(num_within(6,9,12))
print(num_within(3,1,10))

triangle = [[1],[1,1]]
def pascal(n):

  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
 
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]

      length = len(row_prev)+1
      for i in range(length):

        if i == 0:
          row.append(1)

        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])

        else:
          row.append(1)
      triangle.append(row)
      row_number += 1


    for row in triangle:
      print(row)

pascal(1)
pascal(5)