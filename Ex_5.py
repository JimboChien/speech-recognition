import jieba
target = 'loading'
words = jieba.lcut(target)
while(target != 'quit'):
    print("\n請輸入:")
    target = input()
    words = jieba.lcut(target)
    print(words)

