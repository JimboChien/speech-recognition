# -*- coding: utf-8 -*-
import Ex_1,Ex_2
import io
def main():
    target = Ex_1.main()
    #target = input()

    #固定回應區
    f = io.open('keysentence.txt', encoding = 'utf-8-sig')
    keysentence = f.read()
    keysentence = keysentence.split(u'\n')
    f.close()

    f = io.open('reply.txt', encoding = 'utf-8-sig')
    reply = f.read()
    reply = reply.split(u'\n')
    f.close()

    temp_index = 0
    for tempKey in keysentence:
        tempKey = tempKey.split(u'\t')
        for temp in tempKey:
            if(target == temp):
                Ex_2.wordToSound(reply[temp_index])
                print(reply[temp_index])
        temp_index += 1

if __name__ == '__main__':
    main()

