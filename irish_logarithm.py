# https://blog.plover.com/math/irish-logarithm.html


single_digit_numbers = [1,2,3,4,5,6,7,8,9]
t1 = {0: 50} 
used_values = [50]  

available_values = iter(range(99))

for number in single_digit_numbers:
    while True: 
        next_value = next(available_values)
        if next_value not in used_values:
            t1[number] = next_value
            used_values.append(next_value)  
            break  

print(t1)
