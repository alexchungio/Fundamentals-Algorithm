import sys


if __name__ == "__main__":

    while True:
        try:
            num = int(input())
            dict_record = {}
            for i in range(num):
                line = sys.stdin.readline().strip()
                k, v = map(int, list(line.split()))

                if k not in dict_record.keys():
                    dict_record[k] = v
                else:
                    dict_record[k] += v
            for k, v in dict_record.items():
                print(str(k) + ' ' + str(v))
        except Exception as e:
            break
