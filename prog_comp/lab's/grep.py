#!/usr/bin/python3
import sys
from colorama import Fore, Style


def mygrep(p_filename, p_word, tipo=None):
    file = open(p_filename, encoding='UTF-8')
    result_list = []
    numlines = 0
    r = 0
    qt = 0

    for line in file:
        numlines = numlines + 1
        column = line.find(p_word)
        if column >= 0:
            qt += 1
            if tipo == '-n':
                result_list.append([numlines, column])
                print("%s: "  % (Fore.CYAN+str(numlines)+Style.RESET_ALL), end='')
                print("%s"  % line[0:column], end='')
                print("%s"  % Fore.RED+Style.BRIGHT+line[column:column+len(p_word)]+Style.RESET_ALL, end='')
                print("%s"  % line[column+len(p_word):-1])

            if tipo == '-c':
                r = 1

            if tipo is None:
                result_list.append([numlines, column])
                print("%s"  % line[0:column], end='')
                print("%s"  % Fore.RED+Style.BRIGHT+line[column:column+len(p_word)]+Style.RESET_ALL, end='')
                print("%s"  % line[column+len(p_word):-1])

    if r == 1:
        print(f'A quantidade de linhas em que a palavra "{p_word}" foi encontrada é: {qt}')

    return result_list


if len(sys.argv) == 3:
    word = sys.argv[1]
    filename = sys.argv[2]
    result_list = mygrep(filename, word)

if len(sys.argv) == 4:
    word = sys.argv[1]
    filename = sys.argv[2]
    tipos = sys.argv[3]
    result_list = mygrep(filename, word, tipos)
