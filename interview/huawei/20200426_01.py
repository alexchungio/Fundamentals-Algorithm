import sys


def check_primer(m, n):
    """
    求商判断
    :param m:
    :param n:
    :return:
    """
    t = 0
    while(n>0):
        t = m % n
        m = n
        n = t
    if (m==1):
        return True
    else:
        return False


if __name__ == "__main__":

    while True:
        try:
            min_num = int(input())
            max_num = int(input())
            # min_num = 1
            # max_num = 20
            primer_list = []
            for m in range(min_num, int(max_num / (2**0.5))):
                for n in range(m+1, max_num):
                    if check_primer(m, n) is False:
                        continue
                    for q in range(n+1, max_num):
                        if m**2 + n **2 == q**2 and check_primer(q,m) and check_primer(q, n):
                            primer_list.append([m, n, q])
                        else:
                            continue
            if len(primer_list) > 0:
                for primer in primer_list:
                    print("{0} {1} {2}".format(primer[0], primer[1], primer[2]))
            else:
                print('NA')

        except:
            break

