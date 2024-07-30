import pandas as pd

def excel_datas():
    data = pd.read_excel("employee.xlsx")
    # print(data["name"][2])

    rows = len(data.axes[0])
    cols = len(data.axes[1])

    dlst = []
    for r in range(rows):
        data_list = []
        for c in range(cols):
            value = data.iloc[r,c]
            data_list.append(value)
        dlst.append(data_list)
    # print(dlst)
    return dlst

excel_datas()