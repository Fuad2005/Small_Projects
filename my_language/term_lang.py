allowed_calc_ch = set('0123456789+-*/() ')
variable_dict = {}

while True:
    line = input('FD Lang>>> ')

    command, _, rest_of_line = line.rstrip().partition(' ')
    last_ch = line.split()[-1]

    if command == "PRINT":
        if last_ch == '|':
            print(rest_of_line[:-2])
        else:
            pass # I don't know how to implement multiple line commands yet(

    if command == "CALC":
        if last_ch == '|':
            if set(rest_of_line[:-2]).issubset(allowed_calc_ch):
                try:
                    result = eval(rest_of_line[:-2])
                    print(result)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Invalid characters in expression")
        else:
            pass 
    if command == 'ASSIGN':
        if last_ch == '|':
            var, _ ,val = rest_of_line[:-2].partition(' ')
            variable_dict[var] = val
            print(variable_dict)
        else:
            pass




    if line == '\q':
        break