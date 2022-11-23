import os, sys

import win32api, win32con

import time
import sys



print("1.VAC验证错误\n2.VAC无法验证您的游戏会话")

num = input()
# def logs():
#     with open("./log.txt","w") as f:
#         f.write("[time.ctime()]"+)


def inp():
    global file
    global ft
    print("steam路径:?")
    file = input()
    ft = file.endswith(".exe")  # 是否exe后缀


def one():
    print("正在执行方案一···")
    inp()
    os.system("netsh advfirewall set allprofiles state on")
    os.system("bcdedit.exe /set {current} nx alwayson")

    while ft == False:
        win32api.MessageBox(0, "输入包含 steam.exe的路径", "否", win32con.MB_ICONWARNING)
        inp()
    else:
        os.system(file + " /install")
        os.system(file + " /repair")  # 修复SteamService
    os.system('taskkill /f /im %s' % 'kxetray.exe.exe')  # 结束进程
    os.system('taskkill /f /im %s' % 'FlashHelperService.exe')  # 结束进程
    tcf = win32api.MessageBox(0, "是否有效?", "ww", win32con.MB_YESNO)
    if tcf==7:
        win32api.MessageBox(0, "在此期间可能会出现断网", "注意", win32con.MB_ICONASTERISK)
        os.system("netsh winsock reset")




def two():
    inp()
    while ft == False:
        win32api.MessageBox(0, "输入包含 steam.exe的路径", "否", win32con.MB_ICONWARNING)
        inp()
    else:
        os.system('taskkill /f /im %s' % 'steam.exe')  # 结束进程
        os.startfile(file)  # 重调
    tcf = win32api.MessageBox(0, "是否有效?", "ww", win32con.MB_YESNO)
    if tcf==7:
        win32api.MessageBox(0, "在此期间可能会出现断网", "注意", win32con.MB_ICONASTERISK)
        os.system("netsh winsock reset")


if num == "1":
    one()
elif num == "2":
    two()

# def screen():
#     path = 'D:'
#     txt_list = []
#     file_list = os.listdir(path)
#     for i in file_list:
#         file_ext = os.path.splitext(i)
#         front, ext = file_ext
#         if ext == '.fspackage.part':
#             txt_list.append(i)
#     print(txt_list)
#
# screen()
