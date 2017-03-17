from itertools import permutations


def permGene():

    
    file = open(str(input('File path: ')), 'r')
    info = int(file.read())


    count = 0
    number = list(permutations(range(1,info + 1)))


    for i in number:
        count+=1
    print(count)

    for i in number:
        print(' '.join(map(str,i)))


permGene()
