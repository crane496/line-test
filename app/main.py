import math
# import time
def main(argv):
    # start = time.time()
    if len(argv) !=3:
        print("-1")
        exit()
    if not(argv[0].isdigit() and argv[1].isdigit() and argv[2].isdigit()):
        print("-1")
        exit()
    a = int(argv[0])
    b = int(argv[1])
    m = int(argv[2])
    if math.gcd(a,b) != 1:
        print("-1")
        exit()
    prime_count = 0
    n = 0
    b_divisor = factoring(b)
    while(prime_count != m):
        n += 1
        for i in b_divisor:
            if n % i == 0 and b != 1:
                break
        else:
            if is_prime_fast(a*n+b):
                prime_count +=1
    print(a*n+b)
    # elapsed_time = time.time() - start
    # print(elapsed_time)
  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.
def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    else:
        return True

def factoring(b):
    result_array = []
    factor = 2
    while(factor < math.sqrt(b)):
        while(b % factor == 0):
            b = b / factor
            result_array.append(factor)
        factor += 1
    result_array.append(int(b))
    return set(result_array)


def is_prime_fast(q):
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    if pow(2, q-1, q) == 1:
        return is_prime(q)
    return False

# if __name__ == '__main__':
#     input_array = ["105563","125717","760"]
#     main(input_array)
