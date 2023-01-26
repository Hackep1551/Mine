from random import randint
import json
import time

FIELD = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
         '10', '11', '12', '13', '14', '15', '16', '17', '18',
         '19', '20', '21', '22', '23', '24', '25', '26', '27',
         '28', '29', '30', '31', '32', '33', '34', '35', '36',
         '37', '38', '39', '40', '41', '42', '43', '44', '45',
         '46', '47', '48', '49', '50', '51', '52', '53', '54',
         '55', '56', '57', '58', '59', '60', '61', '62', '63',
         '64', '65', '66', '67', '68', '69', '70', '71', '72',
         '73', '74', '75', '76', '77', '78', '79', '80', '81']

FIELD2 = [0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0]

field = FIELD


def field_():
    with open("field.json", "r") as file:
        data = json.load(file)
    return data


def game():
    a = field
    return f'*\t-\t-\t-\t-\t-\t-\t-\t-\t-\t*\n' \
           f'|\t{a[0]}\t{a[1]}\t{a[2]}\t{a[3]}\t{a[4]}\t{a[5]}\t{a[6]}\t{a[7]}\t{a[8]}\t|\n' \
           f'|\t{a[9]}\t{a[10]}\t{a[11]}\t{a[12]}\t{a[13]}\t{a[14]}\t{a[15]}\t{a[16]}\t{a[17]}\t|\n' \
           f'|\t{a[18]}\t{a[19]}\t{a[20]}\t{a[21]}\t{a[22]}\t{a[23]}\t{a[24]}\t{a[25]}\t{a[26]}\t|\n' \
           f'|\t{a[27]}\t{a[28]}\t{a[29]}\t{a[30]}\t{a[31]}\t{a[32]}\t{a[33]}\t{a[34]}\t{a[35]}\t|\n' \
           f'|\t{a[36]}\t{a[37]}\t{a[38]}\t{a[39]}\t{a[40]}\t{a[41]}\t{a[42]}\t{a[43]}\t{a[44]}\t|\n' \
           f'|\t{a[45]}\t{a[46]}\t{a[47]}\t{a[48]}\t{a[49]}\t{a[50]}\t{a[51]}\t{a[52]}\t{a[53]}\t|\n' \
           f'|\t{a[54]}\t{a[55]}\t{a[56]}\t{a[57]}\t{a[58]}\t{a[59]}\t{a[60]}\t{a[61]}\t{a[62]}\t|\n' \
           f'|\t{a[63]}\t{a[64]}\t{a[65]}\t{a[66]}\t{a[67]}\t{a[68]}\t{a[69]}\t{a[70]}\t{a[71]}\t|\n' \
           f'|\t{a[72]}\t{a[73]}\t{a[74]}\t{a[75]}\t{a[76]}\t{a[77]}\t{a[78]}\t{a[79]}\t{a[80]}\t|\n' \
           f'*\t-\t-\t-\t-\t-\t-\t-\t-\t-\t*\n'


def Over():
    a = random_one()
    return f'*\t-\t-\t-\t-\t-\t-\t-\t-\t-\t*\n' \
           f'|\t{a[0]}\t{a[1]}\t{a[2]}\t{a[3]}\t{a[4]}\t{a[5]}\t{a[6]}\t{a[7]}\t{a[8]}\t|\n' \
           f'|\t{a[9]}\t{a[10]}\t{a[11]}\t{a[12]}\t{a[13]}\t{a[14]}\t{a[15]}\t{a[16]}\t{a[17]}\t|\n' \
           f'|\t{a[18]}\t{a[19]}\t{a[20]}\t{a[21]}\t{a[22]}\t{a[23]}\t{a[24]}\t{a[25]}\t{a[26]}\t|\n' \
           f'|\t{a[27]}\t{a[28]}\t{a[29]}\t{a[20]}\t{a[31]}\t{a[32]}\t{a[33]}\t{a[34]}\t{a[35]}\t|\n' \
           f'|\t{a[36]}\t{a[37]}\t{a[38]}\t{a[39]}\t{a[40]}\t{a[41]}\t{a[42]}\t{a[43]}\t{a[44]}\t|\n' \
           f'|\t{a[45]}\t{a[46]}\t{a[47]}\t{a[48]}\t{a[49]}\t{a[50]}\t{a[51]}\t{a[52]}\t{a[53]}\t|\n' \
           f'|\t{a[54]}\t{a[55]}\t{a[56]}\t{a[57]}\t{a[58]}\t{a[59]}\t{a[60]}\t{a[61]}\t{a[62]}\t|\n' \
           f'|\t{a[63]}\t{a[64]}\t{a[65]}\t{a[66]}\t{a[67]}\t{a[68]}\t{a[69]}\t{a[70]}\t{a[71]}\t|\n' \
           f'|\t{a[72]}\t{a[73]}\t{a[74]}\t{a[75]}\t{a[76]}\t{a[77]}\t{a[78]}\t{a[79]}\t{a[80]}\t|\n' \
           f'*\t-\t-\t-\t-\t-\t-\t-\t-\t-\t*\n'


def random_mine():
    i = 10
    a = FIELD2
    while True:
        mine = randint(0, 8)
        if i == 71:
            break
        elif i == 17 or i == 26 or i == 35 or i == 44 or i == 53 or i == 62:
            i += 2
        else:
            if mine == 0:
                a[i] = 'X'
                i += 1
            else:
                i += 1
    return a


def random_one():
    i = 0
    a = random_mine()
    while True:
        if a[i] == 'X':
            if i >= 8 or i <= 16 or i >= 17 or i <= 25 or i >= 26 or i <= 34 or i >= 35 or i <= 43 or i >= 44 or i <= 52 or i >= 53 or i <= 61 or i >= 62 or i <= 70:
                if a[i - 1] != "X":
                    a[i - 1] += 1
                if a[i + 1] != "X":
                    a[i + 1] += 1
                if a[i + 9] != "X":
                    a[i + 9] += 1
                if a[i + 10] != "X":
                    a[i + 10] += 1
                if a[i + 8] != "X":
                    a[i + 8] += 1
                if a[i - 9] != "X":
                    a[i - 9] += 1
                if a[i - 10] != "X":
                    a[i - 10] += 1
                if a[i - 8] != "X":
                    a[i - 8] += 1
                i += 1
            elif i == 0:
                if a[1] != 'X':
                    a[1] += 1
                if a[9] != "X":
                    a[9] += 1
                if a[10] != "X":
                    a[10] += 1
                i += 1
            elif i == 8:
                if a[7] != "X":
                    a[7] += 1
                if a[16] != "X":
                    a[16] += 1
                if a[17] != "X":
                    a[17] += 1
                i += 1
            elif i == 72:
                if a[63] != "X":
                    a[63] += 1
                if a[64] != "X":
                    a[64] += 1
                if a[73] != "X":
                    a[73] += 1
                i += 1
            elif i == 80:
                if a[79] != "X":
                    a[79] += 1
                if a[71] != "X":
                    a[71] += 1
                if a[70] != "X":
                    a[70] += 1
                i += 1
            elif i >= 1 or i <= 7:
                if a[i - 1] != "X":
                    a[i - 1] += 1
                if a[i + 1] != "X":
                    a[i + 1] += 1
                if a[i + 9] != "X":
                    a[i + 9] += 1
                if a[i + 10] != "X":
                    a[i + 10] += 1
                if a[i + 8] != "X":
                    a[i + 8] += 1
                i += 1
            elif i >= 73 or i <= 79:
                if a[i - 1] != "X":
                    a[i - 1] += 1
                if a[i + 1] != "X":
                    a[i + 1] += 1
                if a[i - 9] != "X":
                    a[i - 9] += 1
                if a[i - 10] != "X":
                    a[i - 10] += 1
                if a[i - 8] != "X":
                    a[i - 8] += 1
                i += 1
            elif i == 9 or i == 18 or i == 27 or i == 36 or i == 45 or i == 54 or i == 63:
                if a[i + 1] != "X":
                    a[i + 1] += 1
                if a[i - 9] != "X":
                    a[i - 9] += 1
                if a[i - 8] != "X":
                    a[i - 8] += 1
                if a[i + 9] != "X":
                    a[i + 9] += 1
                if a[i + 10] != "X":
                    a[i + 10] += 1
                i += 1
            elif i == 26 or i == 35 or i == 44 or i == 53 or i == 62 or i == 71 or i == 17:
                if a[i - 1] != "X":
                    a[i - 1] += 1
                if a[i - 9] != "X":
                    a[i - 9] += 1
                if a[i - 10] != "X":
                    a[i - 10] += 1
                if a[i + 9] != "X":
                    a[i + 9] += 1
                if a[i + 8] != "X":
                    a[i + 8] += 1
                i += 1
        elif i == 80:
            break
        else:
            i += 1
    return a


def main():
    score = 0
    a = random_one()
    print(game())
    while True:
        user_input = int(input("Выберите клетку: "))
        user_input -= 1
        b = user_input
        if a[user_input] == "X":
            print(f"Вы проиграли!\n "
                  f"{Over()}"
                  f"Ваш счёт: {score}")
            break
        elif a[user_input] == 3:
            field[b] = 3
            score += 1
            print(game())
        elif a[user_input] == 2:
            field[b] = 2
            score += 1
            print(game())
        elif a[user_input] == 1:
            field[b] = 1
            score += 1
            print(game())
        elif a[user_input] == 0:
            field[b] = 0
            score += 1
            print(game())
        else:
            print("Вы ввели не верное число!\n "
                  "Введите другое число: ")


if __name__ == '__main__':
    main()
