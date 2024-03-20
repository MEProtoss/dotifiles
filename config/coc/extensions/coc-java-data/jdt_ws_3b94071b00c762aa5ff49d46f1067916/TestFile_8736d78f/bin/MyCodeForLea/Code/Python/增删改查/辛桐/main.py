# 2023/06/08 00:33:55
# 请务必安装pandas和matplotlib 这两个库  安装方法 pip install pandas  pip install matplotlib
import matplotlib.pyplot as plt
import pandas as pd


# 定义增加函数
def add_data(df):
    row_index = int(input("请输入要添加数据的行索引："))

    # 如果要添加的行索引超出了 DataFrame 的范围，使用 append() 方法添加新行
    if row_index >= len(df.index):
        # 扩展 DataFrame 的行数，使其能够容纳要添加的行索引
        new_rows = pd.DataFrame(
            index=range(len(df.index), row_index + 1), columns=df.columns
        )
        df = pd.concat([df, new_rows])

    # 获取要添加的数据
    data_to_add = input("请输入要添加的数据，以逗号分隔：")
    data_list = data_to_add.split(",")

    # 添加数据
    df.loc[row_index] = data_list

    # 将修改后的数据保存到 Excel 文件
    df.to_excel(file_name, index=False)

    # 重新读取数据并显示
    df = read_excel(file_name)
    show_data(df)


# 定义修改函数
def modify_data(df):
    # 重新加载数据
    df = read_excel(file_name)
    # 获取要修改数据的起始行索引和结束行索引
    start_row_index = int(input("请输入要修改数据的起始行索引："))
    end_row_index = int(input("请输入要修改的结束行索引："))

    # 检查修改的行是否超出范围
    if end_row_index >= len(df):
        print("错误：要修改的行超出了 Excel 文件的范围！")
        return

    # 获取要修改的数据
    data_to_add = []
    for i in range(start_row_index, end_row_index + 1):
        row_data = []
        for j in range(len(df.columns)):
            column_name = df.columns[j]
            prompt = f"请输入第{i + 1}行，{column_name}列的数据："
            data = input(prompt)
            row_data.append(data)
        data_to_add.append(row_data)

    # 修改数据
    new_rows = pd.DataFrame(data=data_to_add, columns=df.columns)
    df = pd.concat([df.iloc[:start_row_index], new_rows, df.iloc[end_row_index + 1 :]])

    # 将修改后的数据保存到 Excel 文件
    df.to_excel(file_name, index=False)

    # 重新读取数据并显示
    df = read_excel(file_name)
    show_data(df)


# 定义删除函数
def delete_data(df):
    # 重新加载数据
    df = read_excel(file_name)
    # 获取要删除的行
    rows_to_delete = input("请输入要删除的行索引，以逗号分隔：")
    rows_list = rows_to_delete.split(",")
    rows_index = [int(i) for i in rows_list]

    # 删除行
    df = df.drop(rows_index)

    # 保存修改后的数据到 Excel 文件中
    df.to_excel(file_name, index=False)

    # 重新读取数据并显示
    df = read_excel(file_name)
    show_data(df)


# 定义读取Excel文件的函数
def read_excel(file_name):
    df = pd.read_excel(file_name)
    print(f"您已经从文件中读取了{file_name[:-5]}数据")
    return df


# 定义显示 Excel 文件中的数据函数
def show_data(df):
    print("Excel 文件中的数据如下：\n")
    print(df)


# 定义绘制图表函数
def draw_chart(df):
    # 重新读取数据
    df = read_excel(file_name)
    # 获取要绘制图表的列名和索引
    column_name = input("请输入要绘制图表的列名：")
    column_index = int(input("请输入要绘制图表列的索引："))

    # 获取要绘制的图表类型
    chart_type = input("请输入要绘制的图表类型（line/bar/pie）：")

    # 绘制散点图时添加标题和横纵坐标
    if chart_type == "line":
        # 使用 scatter() 方法绘制散点图
        plt.scatter(df.iloc[:, 0], df.iloc[:, column_index], s=50, marker="o")
        # 使用 plot() 方法绘制折线图
        plt.plot(df.iloc[:, 0], df.iloc[:, column_index], linestyle="-")
        plt.xlabel(df.columns[0])
        plt.ylabel(column_name)
        plt.title(f"{column_name} vs. {df.columns[0]}")
        plt.show()

    # 绘制柱状图时添加标题和横纵坐标
    elif chart_type == "bar":
        # 检查要绘制的列中是否有数字数据
        if pd.api.types.is_numeric_dtype(df.iloc[:, column_index]):
            # 使用 bar() 方法绘制柱状图
            plt.bar(df.iloc[:, 0], df.iloc[:, column_index])
            plt.xlabel(df.columns[0])
            plt.ylabel(column_name)
            plt.title(f"{column_name} vs. {df.columns[0]}")
            plt.show()
        else:
            print("要绘制的列中没有数字数据，无法绘制柱状图！")

    # 绘制饼图时添加标题
    elif chart_type == "pie":
        # 检查要绘制的列中是否有数字数据
        if pd.api.types.is_numeric_dtype(df.iloc[:, column_index]):
            # 使用 pie() 方法绘制饼图
            plt.pie(df.iloc[:, column_index], labels=df.iloc[:, 0], autopct="%1.1f%%")
            plt.title(f"{column_name} for {df.columns[0]}")
            plt.show()
        else:
            print("要绘制的列中没有数字数据，无法绘制饼图！")


# 定义功能界面函数
def info_print():
    print("请选择功能--------------")
    print("1. 增加数据")
    print("2. 删除数据")
    print("3. 查询数据")
    print("4. 修改数据")
    print("5. 绘制图表")
    print("6. 退出")
    print("-" * 20)


# 主函数
def main():
    # 读取数据
    content = input("您想处理什么数据（经济/军事/政治）: ")
    global file_name
    if content == "经济":
        file_name = "经济.xlsx"
    elif content == "军事":
        file_name = "军事.xlsx"
    elif content == "政治":
        file_name = "政治.xlsx"
    else:
        print("无效输入！")
        return

    df = read_excel(file_name)
    if df is None:
        return

    # 系统功能需要循环显示，直到用户输入6退出
    while True:
        # 显示功能界面
        info_print()

        # 用户输入功能序号
        user_num = input("请输入功能序号：")

        # 按照用户输入的功能序号, 执行不同的功能（函数）
        if user_num == "1":
            df = read_excel(file_name)

            # 询问是否要添加数据
            add_flag = input("是否要添加数据？（yes or no）：")
            if add_flag == "yes":
                add_data(df)
            else:
                show_data(df)

        elif user_num == "2":
            # 询问是否要删除数据
            del_flag = input("是否要删除数据？（yes or no）：")
            if del_flag == "yes":
                delete_data(df)
            else:
                show_data(df)

        elif user_num == "3":
            # 重新读取数据并显示
            df = read_excel(file_name)
            show_data(df)

        elif user_num == "4":
            show_data(df)
            modify_data(df)

        elif user_num == "5":
            draw_chart(df)

        elif user_num == "6":
            exit_flag = input("确定退出吗？输入(yes or no): ")
            if exit_flag == "yes":
                break
        else:
            print("输入的功能序号有误")


if __name__ == "__main__":
    main()
