'''
Created on Mar 13, 2014

@author: 310122001
'''
"https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/"
"Cubic generator http://www.bogotobogo.com/python/python_generators.php"
def cubic_generator(n):
        for i in range(n):
            yield i ** 3
            
def cubic_not_generator(n):
        listCubes = []
        for i in range(n):
            listCubes.append(i ** 3)
        return listCubes

def sqare_generator():
    for i in range(100):
        yield(i * i)


if __name__ == "__main__":
    print(type(cubic_generator(1)))
    for i in cubic_generator(5):
        print(i, end=' : ')
    print("\nAll generator output is consumed.")
    print(type(cubic_not_generator(5)))
    aList = cubic_not_generator(5)
    for i in aList:
        print(i, end='|')
    aa = sqare_generator()

    print("\n\n next(generator) example")
    try:
        for i in range(10):
            print("Next_1", next(aa))
            for i in range(10):
                    print("Next_2", next(aa))
    except StopIteration:
        print("Ran out of numbers")
