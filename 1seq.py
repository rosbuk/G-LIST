count = '0'
while int(count)<2:
    count = input('Print a number for the length of future list: ')
print('Thank you!')

new_list = []
n=1
while n <= int(count):
    figure = '15'
    while int(figure) not in range(0,10):
        figure = input('Print one figure: ')    
        if not figure.isdigit():
            while not figure.isdigit():
                figure = input('Print one figure: ')
    new_list.append(int(figure))
    n+=1

print(f'That is enough! \nThe new list is {new_list}')
new_list.sort()
print(f'The sorted list is {new_list}')