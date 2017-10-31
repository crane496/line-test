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

  # このコードは引数と標準出力を用いたサンプルコードです。
  # このコードは好きなように編集・削除してもらって構いません。
  # ---
  # This is a sample code to use arguments and outputs.
  # Edit and remove this code as you like.

# if __name__ == '__main__':
#     input_array = ["2","3","1"]
#     main(input_array)
