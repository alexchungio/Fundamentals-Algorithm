import sys

if __name__ == "__main__":

    def swap(lyst, m, n):
        tmp = lyst[m]
        lyst[m] = lyst[n]
        lyst[n] = tmp


    while True:
        try:
            line = input()
            sort_list = []
            for n in list(line)[::-1]:
                if n not in sort_list:
                    sort_list.append(n)
            print(''.join(sort_list))
        except Exception as e:
            break