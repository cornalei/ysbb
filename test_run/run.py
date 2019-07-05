import unittest,subprocess,os,socket
from HTMLTestRunner import HTMLTestRunner
import time,logging
from time import ctime

#bat处理执行时使用
import sys
path='E:\\ysbb' #文件所在根目录
sys.path.append(path)

#指定测试用例和测试报告的路径
test_dir='../test_case'
report_dir='../reports'


def check_port(host, port):
    """检测指定的端口是否被占用"""

    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError:
        print('port %s is available! ' % port)
        return False
    else:
        print('port %s already be in use !' % port)
        return True

# def release_port(port):
#     """释放指定的端口"""
#
#     # 查找对应端口的pid
#     cmd_find = 'netstat -aon | findstr %s' % port
#     print(cmd_find)
#
#     # 返回命令执行后的结果
#     result = os.popen(cmd_find).read()
#     print(result)
#
#     if str(port) and 'LISTENING' in result:
#         # 获取端口对应的pid进程
#         i = result.index('LISTENING')
#         start = i + len('LISTENING') + 7
#         end = result.index('\n')
#         pid = result[start:end]
#
#         # 关闭被占用端口的pid
#         cmd_kill = 'taskkill -f -pid %s' % pid
#         print(cmd_kill)
#         os.popen(cmd_kill)
#
#     else:
#         print('port %s is available !' % port)

def appium_start(host, port):
    bootstrap_port = str(port + 1)
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' % (cmd, ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open('../logs/' + str(port) + '.log', 'a'),
                     stderr=subprocess.STDOUT)


def run_case():
    #加载测试用例
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py') #匹配test开头的用例
    # discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_z_player.py')

    #定义报告的文件格式
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_name=report_dir+'/'+now+' test_report.html'

    #运行用例并生成测试报告
    with open(report_name,'wb') as f:
        runner=HTMLTestRunner(stream=f,title='一说宝宝测试报告',description='一说宝宝安卓版自动化测试报告')
        logging.info('start run test case...')
        runner.run(discover)

def start_appium_action(host,port):
    '''检测端口是否被占用，如果没有被占用则启动appium服务'''
    if check_port(host,port):
        run_case()
        return True
    else:
        appium_start(host, port)
        time.sleep(5)
        return False

def start_devices_action(host,port):
    '''先检测appium服务是否启动成功，启动成功则再启动App'''
    if start_appium_action(host,port):
        print('finis！')
    else:
        run_case()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    start_devices_action(host,port)
