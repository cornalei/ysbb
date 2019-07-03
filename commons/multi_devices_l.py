from appium import webdriver
import yaml
import logging
import logging.config
from time import ctime
import multiprocessing,subprocess

CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired(udid,platformVersion,port):
    with open('../config/ysbb_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=platformVersion
    desired_caps['deviceName']=data['deviceName']
    desired_caps['udid']=udid


    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])
    desired_caps['app'] = app_path

    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    # desired_caps['noReset'] = data['noReset']

    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    print('appium port:%s start run %s at %s' %(port,udid,ctime()))
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',desired_caps)
    driver.implicitly_wait(5)
    return driver

def devices_start_sync(project):
    devices_list = ['VBJ4C18517001054', '8GP7N18504003670']
    version_list = ['9', '8.0.0']

    print('======devices_star_sync===')
    # 构建desired进程组
    desired_process = []
    # 加载desired进程
    for i in range(len(devices_list)):
        port = 4723 + 2 * i
        desired = multiprocessing.Process(target=project, args=(devices_list[i],version_list[i],port))
        desired_process.append(desired)
    # 启动多设备执行进程
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()

def appium_start(host, port):
    bootstrap_port = str(port + 1)
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' % (cmd, ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open('../logs/' + str(port) + '.log', 'a'),
                     stderr=subprocess.STDOUT)


if __name__ == '__main__':
    devices_start_sync(appium_desired)