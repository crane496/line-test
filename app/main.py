import math
def main(argv):
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
    while(prime_count != m):
        n += 1
        if math.gcd(n,b) != 1 and b != 1:
            continue
        if is_prime(a*n+b):
            prime_count +=1
    print(a*n+b)
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

# if __name__ == '__main__':
#     input_array = ["337","743","163"]
#     main(input_array)
