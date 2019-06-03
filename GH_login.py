import http.cookiejar as ht
import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq


class GitHub_login(object):
    def __init__(self):
        ua=UserAgent().random
        self.headers={
            'User-Agent':ua,
            'Referer':'https://github.com/login',
            'Host':'github.com'
        }
    def response_headler(self):
        self.r=requests.Session()
        response=self.r.get('https://github.com/login',headers=self.headers)
        cookis=ht.LWPCookieJar(filename='cookie')
        print(cookis)
        try:
            cookis.load(ignore_discard=True)
        except:
            print('None')
        cookis.save()
        html=pq(response.text)
        authenticity_token=html('#login > form > input[type=hidden]:nth-child(2)').attr('value')
        print(authenticity_token)

        data={
            'commit': 'Sign in',
            'utf8':'✓',
            'authenticity_token':authenticity_token,
            'login':'1737412643@qq.com',
            'password':'c15819285449.',
            'webauthn-support':'supported'
        }
        rs=self.r.post('https://github.com/session',headers=self.headers,data=data)
        re=pq(rs.text)
        print(re('body > div.application-main > div > aside.team-left-column.col-12.col-md-4.col-lg-3.bg-white.border-right.border-bottom.hide-md.hide-sm > div.dashboard-sidebar.js-sticky.top-0.px-3.px-md-4.px-lg-4.overflow-auto.js-pinned-items-reorder-container > div > div > ul > li:nth-child(1) > div > a').text())





    def main(self):
        self.response_headler()

if __name__ == '__main__':
    c=GitHub_login()
    c.main()