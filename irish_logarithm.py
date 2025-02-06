# https://blog.plover.com/math/irish-logarithm.html


single_digit_numbers = [1,2,3,4,5,6,7,8,9]
t1 = {} 
t2 = {}  

available_values = iter(range(99))

for number in single_digit_numbers:
    next_value = next(available_values)
    t1[number] = next_value 

# TODO: we need to construct t2 at the same time. 
# When we add a key:value pair to t1, our lookup table, we also need to calculate all possible results from t1 (aka any t1 key which exists). 


print(t1)
