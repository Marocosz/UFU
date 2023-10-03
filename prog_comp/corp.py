#!/usr/bin/python3
"""
# os.stat(path) = retorna informações estatísticas sobre o path
    # os.stat(path).st_size = tamanho do path

# os.access(path, mode) = Retorna True or False para cada mode
    modes:
    # os.F_OK = Testa a existência do path
    # os.R_OK = Testa a legibilidade do path
    # os.W_OK = Testa a capacidade de escrita do path
    # os.X_OK = Checa se o path pode ser executado

# os.scandir(path) = Retorna entradas de diretório junto com as informações de atributos do path (diretório)
    usando um for conseguimos os nomes dos arquivos do diretório
    # obj.is_dir(follow_symlinks=False) = identificará se é um diretório

# obj.is_file() = Igual o .is_dir, porém que identificará os "não diretórios"

# os.path.splitext(arquivo) = tupla ("caminho", ".ext")
                            ex: ('C:\\Users\\marco\\OneDrive\\Imagens\\3255317', '.jpg')
"""
import os
import sys


def dirfindfiles(ext, path):
    sizesum = 0

    if os.access(path, os.R_OK):
        for obj in os.scandir(path):
            if obj.is_file():

                if os.path.splitext(obj.name)[1].lower() == '.' + ext:
                    sizesum += obj.stat().st_size
                    print(obj.path)

            if obj.is_dir(follow_symlinks=False):
                sizesum += dirfindfiles(ext, obj.path)

    return sizesum


if len(sys.argv) > 1:
    ext = sys.argv[1].lower()
    path = sys.argv[2].lower()
    print(f'{round((dirfindfiles(ext, path) / 1024 ** 3), 3)} Gigabytes')
