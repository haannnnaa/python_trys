def return_42():
    return 42  # An explicit return statement

return_42() 

a = return_42() * 2
c = return_42() + 8
print(a)

#---------------------------------------------------------------------------
def return_hi ():
    return 'hi'
    print('hello')

m = return_hi() * 1
b = return_hi() + 5 # error
print(m)
#---------------------------------------------------------------------------
# returns None
def xx ():
    return

b = xx()

print(b)

#---------------------------------------------------------------------------
m = 4
if 4 in m :
    return 'yes' # error

# ریترن فقط درون تابع کاربرد دارد

#---------------------------------------------------------------------------
def sum (num):
    return num - 2

print(sum(10))
#---------------------------------------------------------------------------
def add (num):
    num += 5
    return num

def first (num):
    if num < 1 :
        return add(num)
    else :
        return num
    
print(first(0))
#---------------------------------------------------------------------------
return_value = print("Hello, World")
# print -> Hello, World

print(return_value)
#---------------------------------------------------------------------------
def sample (num1, num2):
    num1 += 80
    num2 += 30
    return num2, num1

#---------------------------------------------------------------------------
#واریانس
def variance(data, ddof=0):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - ddof)

variance([3, 4, 7, 5, 6, 2, 9, 4, 1, 3])

def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    total_square_dev = sum((x - mean) ** 2 for x in data) #مجموع مجذور انحراف 
    return total_square_dev / (n - ddof)


variance([3, 4, 7, 5, 6, 2, 9, 4, 1, 3])

