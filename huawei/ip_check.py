# Time 2020/04/25 16:54

import sys


def check_ip(ip):

    if len(ip) != 4 or '' in ip:
        return False
    ip = list(map(int, ip))
    for i in range(4):
        if ip[i] < 0 or ip[i] > 255:
            return False
    else:
        return True


def check_mask_ip(ip):

    # check ip valid
    if not check_ip(ip):
        return False

    ip = list(map(int, ip))
    # check ip is all 0 or 255
    if ip in [[0, 0, 0, 0], [255, 255, 255, 255]]:
        return False

    pre_one_all = [255, 254, 252, 248, 240, 224, 192, 128]
    num_flag = 0
    # check last three part
    for num in ip[::-1][:-1]:
        if num == 255:
            num_flag = 255
        if num == num_flag:
            continue
        else:
            return False
    # check the fist part
    if num_flag == 0:
        if ip[0] in pre_one_all:
            return True
        else:
            return False
    elif num_flag == 255:
        if ip[0] == 255:
            return True
        else:
            return False


if __name__ == "__main__":
    num_a, num_b, num_c, num_d, num_e = 0, 0, 0, 0, 0
    num_error, num_private = 0, 0

    while True:
        try:
            line = sys.stdin.readline().strip()
            if line == "":
                break
            ip, mask_ip = line.split('~')

            ip = ip.split('.')
            mask_ip = mask_ip.split('.')

            if check_ip(ip) and check_mask_ip(mask_ip):
                if 1 <= int(ip[0]) <= 126:
                    num_a += 1
                elif 128 <= int(ip[0]) <= 191:
                    num_b += 1
                elif 192 <= int(ip[0]) <= 223:
                    num_c += 1
                elif 224 <= int(ip[0]) <= 239:
                    num_d += 1
                elif 240 <= int(ip[0]) <= 255:
                    num_e += 1

                if int(ip[0]) == 10 or (int(ip[0]) == 172 and 15 < int(ip[1]) < 32) or (
                        int(ip[0]) == 192 and int(ip[1]) == 168):
                    num_private += 1
            else:
                num_error += 1

        except Exception as e:
            print(e)
    print("{0} {1} {2} {3} {4} {5} {6}".format(num_a, num_b, num_c, num_d, num_e, num_error, num_private))
