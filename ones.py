import sys

def divisible_ones(n):
    if n<=1:
        return n
    val = 1
    count = 1

    while (rem_sum != 0):
        val = (val*10 +1) % n
        count += 1
    return count

def main():
    for n in sys.stdin:
        n = int(n.strip())
        print divisible_ones(n)

if __name__ == '__main__':
    main()
