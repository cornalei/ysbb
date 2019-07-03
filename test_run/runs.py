import unittest,socket,multiprocessing
from commons.multi_devices import appium_start
from  BSTestRunner import BSTestRunner
import time,logging

#bat处理执行时使用
import sys
path='E:\\ysbb' #文件所在根目录
sys.path.append(path)

#指定测试用例和测试报告的路径
test_dir='../test_cases'
report_dir='../reports_multi'

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

def start_appium_action(host,port):
    '''检测端口是否被占用，如果没有被占用则启动appium服务'''
    if check_port(host,port):
        return True
    else:
        appium_start(host, port)
        return False

def appium_start_sync():
    print('=====appium_start_sync=====')

    appium_process=[]

    for i in range(2):
        host = '127.0.0.1'
        port = 4725 + 2 * i

        appium = multiprocessing.Process(target=start_appium_action, args=(host, port))
        appium_process.append(appium)

    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()

    time.sleep(5)

def run_case():
    #加载测试用例
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py') #匹配test开头的用例
    # discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_services.py')

    #定义报告的文件格式
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_name=report_dir+'/'+now+' test_report.html'

    #运行用例并生成测试报告
    with open(report_name,'wb') as f:
        runner=BSTestRunner(stream=f,title='一说宝宝测试报告',description='一说宝宝安卓版自动化测试报告')
        logging.info('start run test case...')
        runner.run(discover)

if __name__ == '__main__':
    appium_start_sync()
    run_case()
