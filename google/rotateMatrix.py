#!/usr/bin/python3

def rorateM(m):
    #reverse
    for row in m:
        row = row.reverse()
    return list(map(list,zip(*m)))


if __name__ == '__main__':
    m = [[1,2,3],[4,5,6],[7,8,9]]
    print(rorateM(m))
