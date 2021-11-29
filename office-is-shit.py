"""
2021-11-29

By-: 2045586852@qq.com
office-is-shit.py

introduction：
适用于广东工贸职业技术学院网络自主学习平台
脱离IE实现对信息技术基础网上作业的表单提交 - 阿东

需要注意：
脚本仅为学习参考测试，使用脚本填写数据影响的后果将由使用者承担，
本作不允许用于任何商业用途,同时本软件不承担用户因操作不当对自己和他人造成任何形式的损失或伤害。
"""

from http.cookiejar import Cookie
import requests
import base64
import random,string
import re


#返回随机字符串rn
def getrandomString (a):
    # ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 10)) a-Z0-9
    ran_str = ''.join(random.sample(string.ascii_letters , a)) #a-Z
    #print(ran_str)
    return ran_str
#返回nupa（加密Base64）
def get_upa(user,pw):
    nupa = str(base64.b64encode((str(base64.b64encode(user.encode("utf-8")),"utf-8") + '#' + str(base64.b64encode(pw.encode("utf-8")),"utf-8")).encode("utf-8")),"utf-8")
    return nupa


#login_user = input('请输入登录账号:')
#login_password = input('请输入登录密码:')

login_user = "学号"
#默认密码123456
login_password = "123456"

#设置页数
pidx = 0 
#设置完成页数上限（不超过总页数）
pidx_max = 3
#设置交表延时(s)
post_time = 0
#设置默认7*20任务列表
list_S = [[0 for col in range(7)] for row in range(20)]
#获取登陆Cookies
login_url = 'http://172.100.166.250/Ashx/LoginUser.ashx'
#计算机应用基础课程号
cpa =  "5T5DdiDTMvQ9bLJOZv5VKnn+0U7UP9cS+jBDBfgP1Q/UAW0EdjZRmbkpmgfgl4nkp/z9eodMJN66n/2E78qeQx8PoDtXC7/mVNNPCUvwtPPIpA1r5HahnQ=="
#获取课程交卷地址
score_url = 'http://172.100.166.250/AshxStud/CourseDefTest.ashx'
#请求交卷
post_url = 'http://172.100.166.250/AshxStud/DueScore.ashx'
# 无视题数提交百分卷
post_score = 'DTSAlsZZRp6ZLBF5GvY5waRdYL6JlyS46VRu4okRon90B0pDgsRLin5ICqaxQoU1I1+GnuqNoET7KnhDu/a19elkgHlH2T60SIiSckuV+P4l4ALExMCWkJ1LwAUi2rEK+2SNjio7ErqIq+cQurikpMk76Dal2ZoiYvS0addSKt40rvudDOUy8lq4AdFb/kzlQY5aKQiu9R2FppFjOXjXSmzlXlcR6MVIppOEQAGNG3AwdfN62UgfuYTfsvOXdgoK5xCct08a6cy85CgBKPNmBdHzvfoSqFc8GaM/z2J5hQx/4DBLDfAvyN92pu7cdxkuOaLqicY5aetpi3wuje6C0Uf4dp/SGurmuywttpgymgQSUEgPutncK/eDtJcIKxNpPqcnMrYq40UirU95qAxQHLu+vpC/SDjgzEllitDbp9azA+OseRgsSZtj0yKAwfQqY3V+YIoZX+hjXPKm4Yb76WATEKD9SNAy'
## 填充登陆信息
ndata = {
    "upa" : get_upa(login_user,login_password) ,
    "rn" : getrandomString(10)
}
## 填充post
Sheader = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept' : "text/html, */*; q=0.01",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'X-Requested-With ' : 'XMLHttpRequest',
    #'Referer': 'http://172.100.166.250/Stud/Stud_TCenter.aspx?cpa=5T5DdiDTMvQ9bLJOZv5VKnn%2b0U7UP9cS%2bjBDBfgP1Q%2fUAW0EdjZRmbkpmgfgl4nkp%2fz9eodMJN66n%2f2E78qeQx8PoDtXC7%2fmVNNPCUvwtPPIpA1r5HahnQ%3d%3d&lmidx=4'
    'Accept-Language' : 'zh-Hans-CN,zh-Hans;q=0.5',
    'Accept-Encoding' : 'gzip, deflate',
    'Host' : '172.100.166.250',
    'Connection': 'Keep-Alive',
    'Pragma': 'no-cache'
}

## 填充get
uheader = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept' : 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection' : 'Keep-Alive'
}

"""
正确登陆时将获取如下信息
print (login.cookies) :
console:
200
1|Stud%2fDefault.aspx
<RequestsCookieJar[<Cookie ncptuserinfo=LuiQ8jb06%2bRGaDHgJG3kV%2bUoVsd5tLlF for 172.100.166.250/>]> 
"""

print("正在登陆！")

login = requests.get(login_url,params=ndata)
cookie = requests.utils.dict_from_cookiejar(login.cookies)


for pidx in range(1,pidx_max + 1) :
    print("正在获取本课程第" + str(pidx) + "页任务列表")
    udata = {
        "pidx" : pidx,
        "ct" : "3",
        "cpa" : cpa,
        "ttype" : "28",
        "ppa" : "",
        "rn" : getrandomString (10)
    }

    # 获取任务页任务
    score = requests.get(score_url,params=udata,headers=uheader,cookies=cookie)
    # 设置正则格式
    reg = u"(?<=test_ch_stud\(\')(.*?)(?=',)"
    # 获取当页任务列表
    list_S = re.findall(reg,score.text)
    print("正在完成第" + str(pidx) + "页任务列表")
    for i in range(0,20):
        Sdata = {
            'upa':list_S[i],
            'score' : post_score,
            'cmd' : '3',
            'tms' : '0',
            'rn' : getrandomString(10)
        }
        S = requests.post(post_url,headers=Sheader,data=Sdata,cookies=cookie)
        print('第' + str(pidx) + '页任务' + str(i + 1) + "已完成，进行延迟中    " + str(post_time) + '秒开始下一题')
        time.sleep(post_time)
    #    aaaa = S.content.decode("utf-8")
    print('已完成第' + str(pidx) + '页任务列表')
print('已完成指定操作，请登录平台查看成绩。')
