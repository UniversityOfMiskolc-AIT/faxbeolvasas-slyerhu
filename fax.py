__author__ = "Szilveszter Rafael Szabo"
__version__ = "1.0.0"
__email__ = "ssrofficial@gmail.com"
__neptun__ = "YTBR1C"


def parse_number(row,col,raw_data):
    """Returns a digit from read data

    Keyword arguments: 
    row --  starting line of account number
    col -- the exact number from range 1-9 
    raw_data -- the file that has been read
    """
    num0 = ' _ ' \
           '| |' \
           '|_|'

    num1 = '   ' \
           '  |' \
           '  |'

    num2 = ' _ ' \
           ' _|' \
           '|_ '

    num3 = ' _ ' \
           ' _|' \
           ' _|'

    num4 = '   ' \
           '|_|' \
           '  |'

    num5 = ' _ ' \
           '|_ ' \
           ' _|'

    num6 = ' _ ' \
           '|_ ' \
           '|_|'

    num7 = ' _ ' \
           '  |' \
           '  |'

    num8 = ' _ ' \
           '|_|' \
           '|_|'

    num9 = ' _ ' \
           '|_|' \
           ' _|'

    numbers = {
        num0 : 0,
        num1 : 1,
        num2 : 2,
        num3 : 3,
        num4 : 4,
        num5 : 5,
        num6 : 6,
        num7 : 7,
        num8 : 8,
        num9 : 9
    }

    row_shift = row * 4
    col_shift = col * 3

    first = raw_data[0 + row_shift][col_shift - 3 : col_shift]
    second = raw_data[1 + row_shift][col_shift - 3 : col_shift]
    third = raw_data[2 + row_shift][col_shift - 3 : col_shift]

    raw_number = first + second + third

    try:
        return numbers[raw_number]
    except KeyError:
        return "?"


def get_account_number(raw_data):
    """Returns how many account number is in the file

    Keyword arguments: 
    raw_data -- the file that has been read
    """
    return len(raw_data)//4


def read_file(file):
    """Reading file

    Keyword arguments: 
    file -- the file that has to be read e.g.: "accounts.txt"
    """
    with open(file) as f:
        return f.readlines()


def check_converted_account(converted_account):
    """Calculates checksum from the converted account number and checks it

    Keyword arguments: 
    converted_account -- the converted number e.g.: 123456789
    """
    checksum = 0
    if "?" in converted_account:
        return str(converted_account) + " ILL"
    else:
        for i,j in zip(converted_account, range(1,10)):
            checksum += int(i) * j
        if (checksum % 11) == 0:
            return str(converted_account)
        else:
            return str(converted_account) + " ERR"
           



def main():
    #Print metadata
    print("Author: " + __author__)
    print("Neptun: " + __neptun__)
    print("Version: " + __version__)
    print("E-mail: " + __email__ + "\n")

    #Reading data and get account numbers
    data = read_file("numbers.txt")
    accounts = get_account_number(data)
    full_parsed = []

    #Parsing, checking, printing data
    for account_number in range(accounts):
        converted_account = []
        for number in range(1,10):
            converted_number = parse_number(account_number, number, data)
            converted_account.append(converted_number)
        
        copy = converted_account
        values = ''.join(str(v) for v in copy) # For nice output
        checked = check_converted_account(values)
        print(checked)

if __name__ == "__main__":
    main()
 