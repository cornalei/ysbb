import unittest,subprocess,os,socket
from time import ctime
from HTMLTestRunner_cn import HTMLTestRunner
import time,logging
import smtplib                           #发送邮件模块
from email.mime.text import MIMEText    #定义邮件内容
from email.header import Header         #定义邮件标题
from email.mime.multipart import MIMEMultipart  #用于传送附件
# bat处理执行时使用
import sys

path = 'E:\\ysbb'  # 文件所在根目录
sys.path.append(path)

# 指定测试用例和测试报告的路径
test_dir = '../test_case'
report_dir = '../reports'
def run_case():
    #加载测试用例
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py') #匹配test开头的用例
    # discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_z_player.py')

    #定义报告的文件格式
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_name=report_dir+'/'+now+' test_report.html'

    #运行用例并生成测试报告
    with open(report_name,'wb') as f:
        runner=HTMLTestRunner(stream=f,title='一说宝宝测试报告',description='一说宝宝安卓版自动化测试报告',verbosity=2, retry=1, save_last_try=True)
        logging.info('start run test case...')
        runner.run(discover)

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

def appium_start(host, port):
    bootstrap_port = str(port + 1)
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' % (cmd, ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open('../logs/' + str(port) + '.log', 'a'),
                     stderr=subprocess.STDOUT)

def send_mail(latest_report):
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()

    # 发送邮箱服务器
    # smtpserver='smtp.163.com'
    smtpserver = 'smtp.exmail.qq.com'

    # 发送邮箱用户名密码
    # user='leilei3356@163.com'
    # password='leilei123456'
    user = 'leil@excetop.com'
    password = 'Yj72bTdyBrEkzYZs'

    # 发送和接收邮箱
    sender = 'leil@excetop.com'
    receives = ['leil@excetop.com']
    # receives = ['1591505373@qq.com', 'leilei3356@163.com']

    # 发送邮件主题和内容
    subject = '一说宝宝安卓自动化测试报告'

    # 构造附件内容
    send_file = open(latest_report, 'rb').read()
    att = MIMEText(send_file, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="test_report.html"'

    # 构建发送与接收信息
    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(mail_content, 'html', 'utf-8'))
    msgRoot['subject'] = Header(subject, 'utf-8')
    msgRoot['From'] = sender
    msgRoot['To'] = ','.join(receives)
    msgRoot.attach(att)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # HELO 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("Start send Email...")
    smtp.sendmail(sender, receives, msgRoot.as_string())
    smtp.quit()
    print("Send Email end!")

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print(("new report is :" + lists[-1]))

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

def start_appium_action(host,port):
    '''检测端口是否被占用，如果没有被占用则启动appium服务'''
    if check_port(host,port):
        run_case()
        return True
    else:
        appium_start(host, port)
        time.sleep(10)
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
    start_devices_action(host, port)
    # h获取最新测试报告
    latest_report = latest_report(report_dir)
    # 发送邮件报告
    send_mail(latest_report)
