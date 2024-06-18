def main():
    number = int(input("enter an integer"))
    memo_size = int(input("enter the number of bits"))
    if number > 2**memo_size-1:
        print("you liar! either the number or the memory size is wrong!")
    else:
        binaryNegativeNum(number, memo_size)

def binaryNegativeNum(number, memo_size):
    B_num = []
    B_NegNum = []
    flag = True

    for i in range(memo_size-1, -1, -1):
        if number >= 2**i:
            number -= 2**i
            B_num.append("1")
        else:
            B_num.append("0")
    
    for i in range(memo_size):
        if B_num[i] == "1":
            B_NegNum.append("0")
        else:
            B_NegNum.append("1")
    
    for i in range(memo_size-1, -1, -1):
        if flag:
            if B_NegNum[i] == "1":
                B_NegNum[i] = "0"
            else:
                B_NegNum[i] = "1"
                flag = False
    print("".join(B_NegNum))
main()
