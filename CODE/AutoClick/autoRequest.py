import pandas as pd
import numpy as np
from uiautomation import WindowControl, MenuControl
wx = WindowControl(Name='微信',  searchDepth=1)
wx.SwitchToThisWindow()  # 切换到主窗口
hw = wx.ListControl(Name='会话')
df = pd.read_excel(r'./123.xlsx')
while True:
    we = hw.TextControl(searchDepth=4)  # 查找未读消息
    if we.Name:
        we.Click(simulateMove=False)  # 点击未读消息
        last_msg = wx.ListControl(Name='消息').GetChildren()[-1].Name  # 读取最近一条消息
        msg = df.apply(lambda x: x['回复内容'] if x['关键词'] in last_msg else None, axis=1)
        msg.dropna(axis=0, how='any', inplace=True)  # 数据清洗，移除空白数据
        ar = np.array(msg).tolist()  # 数据转字符串
        if ar:
            # 如果有关键字
            wx.SendKeys(ar[0].replace('{br}', '{Shift}{Enter}'), waitTime=0)  # 讲结果输入文字框
            wx.SendKeys('{Enter}', waitTime=0)  # 模拟回车
            wx.TextControl(SubName=ar[0][:5]).RightClick()  # 通过消息匹配检索会话框联系人并右击
        else:
            wx.TextControl(SubName=last_msg[:5]).RightClick()
        ment = MenuControl(ClassName="CMenuWnd")  # 匹配右击控件
        ment.TextControl(Name='不显示聊天').Click()


