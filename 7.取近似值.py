## 题目描述
      # 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
## 输入描述:
      # 输入一个正浮点数值
## 输出描述:
      # 输出该数值的近似整数值


while True:
    try:
        i = input()
        if "." in i:
            if len(i)-i.index(".") > 2:
                print("请输入到小数点后一位")
            else:
                if int(i[i.index(".")+1]) >= 5:
                    print(int(float(i))+1)
                else:
                    print(int(float(i)))
        else:
            print(i)
    except:
        break
