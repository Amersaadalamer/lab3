def q1(s, index):
    try:
        return s[index]
    except IndexError:
        return "Index out of range"
pass



def q2(n):
    if n < 0:
        return "negative number"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
pass



def q3(lst):
    total = 0
    for num in lst:
        total += num
    return total
pass



def q4(name, age):
    return "My name is " + name + " and I am " + str(age) + " years old."
pass


   

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        print('Execution started...')
       
        result = func(*args, **kwargs)
       
        print('Execution ended!')
       
        return result
    return wrapper

@log_execution_time
def q5(a, b):
    print(f"The sum is: {a + b}")
pass
