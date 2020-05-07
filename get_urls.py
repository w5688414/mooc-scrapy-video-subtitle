import requests,json

headers = {
"accept": "*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
"content-length": "16",
"content-type": "application/x-www-form-urlencoded;charset=UTF-8",
"cookie": 'EDUWEBDEVICE=0edd48eedc584cb0aca9784c215375af; hb_MA-A976-948FFA05E931_source=github.com; __yadk_uid=8EghquwxG4eDib5D9QY9mBtwFkKzFnkd; P_INFO=m15623211472@163.com|1587861357|1|imooc|00&99|bej&1587825426&mail163#bej&null#10#0#0|156472&1|mailmaster_android&mail163&mail163_qrcode&note_client|15623211472@163.com; bpmns=1; hasVolume=true; videoVolume=0.8; NTESSTUDYSI=a18b955a5a324814b12b87b80d66b5b2; STUDY_INFO="m15623211472@163.com|-1|2463286|1588819720864"; STUDY_SESS="yXgjDpX7UsdLjfb/CEn9UPtuJXWxPH7GvJORXC/Ev//O7EvBc70JWjZ01iaXaICKs5q4SGijMQK7S+aKh0vnRfv5GVWv326h9xRqsOevsE9Ge5fa5zJbtHkVCrYXEmJRxyX4YZLG34YaZLFkQxddsZ8wZjW7qFjB45xdFjxtvSAnppr6KrivyjY6FmKs/Qou"; STUDY_PERSIST="ZrXi496IRwrnoZKHpz7OpVRWA7fx7oOcVT62cYZGFK8Ih1zAABUZ0l8C0KSQbd6S+tBNSaAmfnWWrsFHgA2E1+xPvSmCY2VsOM0hVGW2yG9UHLsRG9mEIHrVBPL/8e3NCPOr8YHaTa0wLaO3ZSjfNF/zhxHcRCSg/csCg1mjauxvdPp6WlIa3WTPU+ilCbJUlCBXJFYcQ+vZCYYUbNiW9mSi35XlbUYrsuDjWiHj351OSdFA6J5jrZLCRv8JU8qN8WQLi3xTJ45sq/acjsEWiA=="; NETEASE_WDA_UID=2463286#|#1407305407235; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1587721658,1587861333,1588819722; WM_NI=7RgeCPd3EId0JbfwmowL1vvZIjEHJq3pdNlLJScX%2FsJgJYbqYFTg5gTSxtV91xNCgpr7BKSMBRWGzrZ8XMAH4RIjZA85sZX0Al9twpSMPhRPwjvLVXF6tnmeKhxLSoRWWE8%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee91b3439695f79bae72b6eb8fb2d15f838a9faaf15be9a7a3b2e2709cbafe96d92af0fea7c3b92af58ea986c25ca8ed8baae73c8abeaa98f065b594ff97f5528bb68ba9c97bf1b0acafef488a8dadb9ae798ab986bae17b9b9a9c88b86d988db895d533f3a882a4e67cb2e98eacd247828e99a8f97a9ae898aec444f88e878bd94bfcebbdbbdb3c83b4f795f67c9193a089d15cb5b6baadd55486eabc8ff06f89b8b8add265928999a6bb37e2a3; WM_TID=Zeiyq8crmghAVRFVRUY6RZSYYznffZki; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1588819797',
"edu-script-token": "a18b955a5a324814b12b87b80d66b5b2",
"origin": "https://www.icourse163.org",
"referer": "https://www.icourse163.org/channel/2001.htm",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
url_json = 'https://www.icourse163.org/web/j/courseBean.getMocTermStatisticListByParms.rpc'
# data_json = json.dumps({'key1':'value1','key2':'value2'})   #dumps：将python对象解码为json数据
requestdata='csrfKey=a18b955a5a324814b12b87b80d66b5b2'
r_json = requests.post(url_json,data=requestdata,headers=headers)
print(r_json)
print(r_json.text)
print(r_json.content)

with open('./data.json', 'w') as json_file:
        json_file.write(r_json.text)