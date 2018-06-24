from sys import argv

from numpy import sum, zeros, array


def generate_square(val):
    magicSquare = zeros((val, val))

    val_s = val ** 2

    i = int(val / 2)
    j = val - 1

    num = 1
    while num <= val_s:
        if i == -1 and j == val:
            j = val - 2
            i = 0
        else:
            if j == val:
                j = 0
            if i < 0:
                i = val - 1

        if magicSquare[i, j]:
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[i, j] = num
            num += 1

        j = j + 1
        i = i - 1
    return magicSquare.astype(int)


def check_square(square):
    x = len(square)

    control_sum = sum(square[0])

    diag1 = 0
    diag2 = 0

    for i in range(x):
        magic = sum(square[i]) == control_sum
        if not magic:
            return False, -1
        magic = sum(square[:, i]) == control_sum
        if not magic:
            return False, -1
        diag1 += square[i, i]
        diag2 += square[i, x - i - 1]

    magic = diag1 == diag2 == control_sum
    if magic:
        return magic, control_sum
    else:
        return magic, -1


if __name__ == '__main__':
    if argv[1] == 'generate':
        print(' ' + str(generate_square(int(argv[2]))).replace("[", '').replace(']', ''))
    elif argv[1] == 'check':
        l = int(argv[2])
        square_string = str.split(argv[3], " ")
        square_list = []
        for i in range(l):
            square_list.append(square_string[l * i: l * (i + 1)])
        square = array(square_list).astype(int)

        print(check_square(square))
