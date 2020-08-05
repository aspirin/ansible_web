import threading
import subprocess
import requests
import json
import time
import logging
logger = logging.getLogger("mydjango")
class Deploy(threading.Thread):
    def __init__(self):
        self.shell = ''
        self.ansible_cwd = ''
        self.ansible_module = ''
        threading.Thread.__init__(self)
    def run(self):

        logger.info("start.... %s,%s"%(self.getName(),self.shell))
        r = subprocess.call("sh " + self.shell + " 1> out"+self.shell+".log 2> error"+self.shell+".log", cwd=self.ansible_cwd, shell=True)
        # if r == 0:
        #    dingmessage()
        if r == 0:
            dingmessage(self.ansible_module+"发布成功")
            logger.info('执行成功')
        else:
            dingmessage(self.ansible_module+"发布失败")
            logger.info('执行失败')
        logger.info("end.... %s"%(self.getName(),))




def dingmessage(_msg):
    # 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=a2ca931da90062f5ab23497026c45d87695bf5ddda1098d545e690e390b2ff89"
    #构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    #构建请求数据
    tex = "简账云测试版发布提醒"
    message ={
        "msgtype": "markdown",
        "markdown": {
            "title": tex,
            "text": "#### 简账云测试版 @all \n> 简账云最新版:"+_msg+" \n> ###### By 简账钉钉机器人 \n"
        },
        "at": {
            "isAtAll": True
        }
    }
    #对请求的数据进行json封装
    message_json = json.dumps(message)
    #发送请求
    info = requests.post(url=webhook,data=message_json,headers=header)
    #打印返回的结果
    print(info.text)