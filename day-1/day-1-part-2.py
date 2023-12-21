def main():

    num_list = []

    alpha_three = ['one', 'two', 'six']
    alpha_four = ['zero', 'four', 'five', 'nine']
    alpha_five = ['three', 'seven', 'eight']

    alpha_num_dict = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }

    with open('day-1-inputs.txt', 'r') as f:
        for line in f:
            
            first_digit = ''
            last_digit = ''

            line_length = len(line)

            for x in range(0, line_length-1):
                if first_digit == '':

                    if line[x].isdigit():
                        first_digit = line[x]
                
                    elif line[x:x+3] in alpha_three:
                        first_digit = alpha_num_dict[line[x:x+3]]
                    
                    elif line[x:x+4] in alpha_four:
                        first_digit = alpha_num_dict[line[x:x+4]]

                    elif line[x:x+5] in alpha_five:
                        first_digit = alpha_num_dict[line[x:x+5]]

                else:

                    if line[x].isdigit():
                        last_digit = line[x]
                
                    elif line[x:x+3] in alpha_three:
                        last_digit = alpha_num_dict[line[x:x+3]]
                    
                    elif line[x:x+4] in alpha_four:
                        last_digit = alpha_num_dict[line[x:x+4]]

                    elif line[x:x+5] in alpha_five:
                        last_digit = alpha_num_dict[line[x:x+5]]
            
            if last_digit == '':
                last_digit = first_digit
                
            num = int(first_digit + last_digit)

            num_list.append(num)
    
    answer = sum(num_list)
    print(answer)


if __name__ == "__main__":
    main()
