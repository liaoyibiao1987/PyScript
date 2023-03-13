#!/usr/local/bin/python3
# coding=utf-8

import requests
import json
import smtplib
import jinja2
import os.path as pth
import time
from email.mime.text import MIMEText
from email.header import Header

HEFEN_D = pth.abspath(pth.dirname(__file__))
LOCATION = '珠海'
LOCATIONID = 'CN101280701'
ORIGINAL_URL = 'https://free-api.heweather.com/s6/weather/forecast?parameters'
TO = ['zlyun616@live.com','zlyun616@gmail.com']


def sendEmail(content, title, from_name, from_address, to_address, serverport, serverip, username, password):
  msg = MIMEText(content, _subtype='html',_charset='utf-8')
  msg['Subject'] = Header(title, 'utf-8')
  # 这里的to_address只用于显示，必须是一个string
  msg['To'] = ','.join(to_address)
  msg['From'] = from_name
  try:
    s = smtplib.SMTP_SSL(serverip, serverport)
    s.login(username, password)
    # 这里的to_address是真正需要发送的到的mail邮箱地址需要的是一个list
    x = s.sendmail(from_address, to_address, msg.as_string())
    print('%s----发送邮件成功' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
  except Exception as err:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(err)

def get_data():
  new_data = []
  parametres = {
    'location': LOCATIONID,
    'key': '2229bac5140f4891817728764f7ce087', #注册和风天气会给你一个KEY
    'lang': 'zh',
    'unit': 'm'
  }

  try:
    response = requests.get(ORIGINAL_URL,params=parametres)
    r = json.loads(json.dumps(response.text,ensure_ascii=False,indent=1))
    r = json.loads(response.text)
  except Exception as err:
    print(err)

  weather_forecast = r['HeWeather6'][0]['daily_forecast']
  for data in weather_forecast:
    new_obj = {}
    # 日期
    new_obj['date'] = data['date']
    # 日出时间
    new_obj['sr'] = data['sr']
    # 日落时间
    new_obj['ss'] = data['ss']
    # 最高温度
    new_obj['tmp_max'] = data['tmp_max']
    # 最低温度
    new_obj['tmp_min'] = data['tmp_min']
    # 白天天气状况描述
    new_obj['cond_txt_d'] = data['cond_txt_d']
    # 风向
    new_obj['wind_dir'] = data['wind_dir']
    # 风力
    new_obj['wind_sc'] = data['wind_sc']
    # 降水概率
    new_obj['pop'] = data['pop']
    # 能见度
    new_obj['vis'] = data['vis']

    new_data.append(new_obj)
  return new_data



def render_mail(data):
  env = jinja2.Environment(loader = jinja2.FileSystemLoader(HEFEN_D))
  return env.get_template('hefentianqi.html').render({'data': data})

def main():
  config = {
  "from": "327648349@qq.com",
  "from_name": '预报君',
  "to": TO,
  "serverip": "smtp.qq.com",
  "serverport": "465",
  "username": "327648349@qq.com",
  "password": "piyejgrpgjdfbgcf" #QQ邮箱的SMTP授权码
  }

  title = "马哥！我不是垃圾！"

  data = get_data()
  body = render_mail(data)
  sendEmail(body, title, config['from_name'], config['from'], config['to'], config['serverport'], config['serverip'], config['username'], config['password'])

if __name__ == '__main__':
  main()