while True:
    # 接收用户输入
    user_input = input("请输入命令 (q 退出): ")

    if user_input == "q":
        print("程序已退出。")
        break
    elif user_input == "hello":
        print("你好！")
    elif user_input == "calculate":
        # 接收用户输入的数字
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        operation = input("请输入操作 (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "除数不能为零"
        else:
            result = "无效的操作符"

        print("结果:", result)
    else:
        print("未知命令，请重试。")
