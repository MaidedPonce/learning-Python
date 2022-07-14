def run():
    
    for i in range(1, 100):
        if i % 2 != 0:
            continue
        print(i)

def run2():

    nombre = input("Escribe tu nombre:D ")

    for i in nombre:
        if i == "A":
            break
        print(i)

if __name__ == '__main__':
    run2()