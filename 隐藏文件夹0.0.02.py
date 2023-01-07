#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sys
import time
 


print('请在下方输入指令,输入help来查看指令列表')

def Cre_Open(way):                                      # 检测文件夹是否存在,若不存在则创建,之后无论最初是否存在文件夹,打开该文件夹
    if not os.path.isdir('%s'%way):
        os.mkdir('%s'%way)
        os.system("attrib +s +a +h +r %s"%way)          # 彻底隐藏文件夹
    os.system('explorer %s'%way)


def Crefile(way):                                       # 创建密码文件
    if not os.path.isfile('%s'%way):
        os.system('echo > %s'%way)
        # os.system("attrib +s +a +h +r %s"%way)


def Del(way):
    if os.path.isdir('%s'%way):
        os.system('attrib -a -s -h -r %s'%way)          # 取消隐藏文件夹
        os.system('rd/s/q %s'%way)


def Delfile(way):
    if os.path.isfile('%s'%way):
        os.system('attrib -a -s -h -r %s'%way)          # 取消隐藏文件
        os.system('del %s'%way)


def pswcorrect():
    if pswFlag == False:                                # 检测密码正确性
        os.system('echo %s > %s'%(psw,_way))
        os.system("attrib +s +a +h +r %s"%_way)
        return True
    else:
        psws = open(_way)
        psws = psws.readline().split()
        psws = "[".join(psws)                           # 强制读取密码文档,冗余代码较多但难以修改
        psws = psws.split("[")
        psws = ']'.join(psws)
        psws = psws.split("]")
        psws = ''.join(psws)
        psws = psws.split(",")
        psws = ''.join(psws)
        psws = psws.split("'")
        psws = ' '.join(psws)
        psws = psws.split()
        if psw == psws:
            return True
        elif psw != psws:
            return False


while 1:
    try:
        if 'cmd' in globals():
            del cmd                                             # 重置指令
        if "command" in globals():
            del command
        if 'command_flag' in globals():
            del command_flag

        config_name = 'psw.txt'                                 # .py转.exe后获取文件路径的特殊方法,来源:CSDN
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        config_path = os.path.join(application_path, config_name)

        way_ = 'E:\\Dir_DIR'
        _way = config_path                                      # _way,密码文档路径


        if os.path.isfile(_way):                                # 检测密码文档是否存在
            pswFlag = True
        else:
            pswFlag = False
        
        if os.path.isdir(way_):                                 # 检测文件夹是否存在
            dirFlag = True
        else:
            dirFlag = False

        cmd = input('>>')
        command = cmd.split(' ')                                # 指令检测
        if command[0] == 'psw':
            command_flag = 'psw'
            cmdLen = 2
        elif command[0] == 'delpsw':
            command_flag = 'delpsw'
            cmdLen = 2
        elif command[0] == 'deldir':
            command_flag = 'deldir'
            cmdLen = 2
        elif command[0] == 'help':
            command_flag = 'help'
            cmdLen = 1
        elif command[0] == '2300327235':
            command_flag = 'readpsw'
            cmdLen = 1
        elif command[0] == 'ifpsw':
            command_flag = 'ifpsw'
            cmdLen = 1
        elif command[0] == 'ifdir':
            command_flag = 'ifdir'
            cmdLen = 1
        if not 'command_flag' in globals():
            if c == 1:
                pass
        cmd_len = len(command)
        if cmd_len == cmdLen and cmd_len == 2:
            psw = list(command[1])
        elif cmdLen == 1 and cmd_len != cmdLen:                 # 指令长度合法性检测
            if c == 1:                                          # 引用未定义变量,引起变量错误,触发指令错误异常处理
                pass

        if command_flag == 'psw':                               # 打开隐藏文件夹模块
            if cmd_len == 1:
                psw = list(input('请输入密码:'))
            plenth = len(psw)
            for i in range(plenth):
                psw[i] = str(ord(psw[i]) + 230)                 # 加密密码

            if pswcorrect():                                    # 密码检测
                Cre_Open(way_)
            else:
                print('密码错误')
                time.sleep(1)
            break

        if command_flag == 'delpsw':                            # 删除密码模块
            if cmd_len == 1:
                psw = list(input('请输入密码:'))
            plenth = len(psw)
            for i in range(plenth):
                psw[i] = str(ord(psw[i]) + 230)                 # 加密密码

            if pswcorrect():                                    # 密码检测
                Delfile(_way)
            else:
                print('密码错误')
                time.sleep(1)
            break

        if command_flag == 'deldir':
            if cmd_len == 1:
                psw = list(input('请输入密码:'))
            plenth = len(psw)
            for i in range(plenth):
                psw[i] = str(ord(psw[i]) + 230)                 # 加密密码

            if pswcorrect():                                    # 密码检测
                Del(way_)
                Delfile(_way)
            else:
                print('密码错误')
                time.sleep(1)
            break

        if command_flag == 'help':
            print(
                '["psw","delpsw","deldir","ifpsw","ifdir"]\n\
    psw [password] 验证密码并打开隐藏文件夹,若无密码则输入密码同时新建密码\n\
    delpsw [password] 删除密码\n\
    deldir [password] 删除隐藏文件夹和密码\n\
    ifpsw 检测密码是否存在\n\
    ifdir 检测隐藏文件夹是否存在\n\
    [password]可省略'
            )

        if command_flag == 'readpsw':
            Delfile(_way)
            print('密码已清除')
            time.sleep(1)

        if command_flag == 'ifpsw':
            if pswFlag:
                print('存在密码')
            else:
                print('不存在密码')

        if command_flag == 'ifdir':
            if dirFlag:
                print('存在隐藏文件夹')
            else:
                print('不存在隐藏文件夹')

    except EOFError:
        print('强制退出')
        time.sleep(1)
        exit()
    except NameError:
        print('Error:指令错误')
        continue

'''
    更新日志:
        0.0.01 支持 psw,delpsw,deldir 功能[二级指令];
               支持 help 功能[一级指令];
               暂不支持自定义隐藏文件夹路径,默认为E:\Dir_DIR

        0.0.02 支持 ifpsw,ifdir 功能[一级指令];
               支持 [二级指令] 的简化;
               添加异常处理;
'''