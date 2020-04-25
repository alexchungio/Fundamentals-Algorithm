import sys



if __name__ == "__main__":

    # method 1
    while True:
        try:
            n = int(input())
            prime_list = []
            for i in range(2, (n//2 + 1)):
                while n % i == 0:
                    n /= i
                    prime_list.append(i)

            if prime_list:
                print(" ".join(map(str, prime_list)))
            else:
                print(str(n) + ' ')
        except:
            break

    # method 2
    while True:
        try:
            n = int(input())
            prime_list = ''
            for i in range(2, (n // 2 + 1)):
                while n % i == 0:
                    n /= i
                    prime_list += str(i) + ' '

            if len(prime_list) != 0:
                print(prime_list)
            else:
                print(str(n) + ' ')
        except:
            break



