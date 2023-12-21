def main():

    # empty list of numbers
    num_list = []

    # read file
    with open('day-1-inputs.txt', 'r') as f:

        # read line
        for line in f:
            
            first_digit = ''
            last_digit = ''

            for char in line:
                if char.isdigit() and first_digit == '':
                    first_digit = char
                elif char.isdigit():
                    last_digit = char
            
            if last_digit == '':
                last_digit = first_digit
            
            num = int(first_digit + last_digit)

            num_list.append(num)
    
    # sum the numbers
    answer = sum(num_list)
    print(answer)


if __name__ == "__main__":
    main()
