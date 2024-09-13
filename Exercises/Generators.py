def gen_fib_numbers(limit):
    a, b = 0, 1
    while b <= limit + 1:
        yield b
        a, b = b, a + b

def main():
    print('Start')
    for i in gen_fib_numbers(5): print(i)

if __name__ == "__main__":
    main()