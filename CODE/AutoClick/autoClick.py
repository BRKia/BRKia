from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

print('请提前打开微信聊天框！')
a = input('输入内容：')
b = eval(input('发多少条？'))
print('数据已接收，请将光标移至会话框！')
time.sleep(2)
for i in range(3):
    print(r'距离程序运行还有%d秒！' %(3 - i))
    time.sleep(1)
for i in range(b):
    print('发送第', i + 1, '条微信')
    keyboard.type(a)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
print('消息发送成功')


