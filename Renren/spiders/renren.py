#coding:utf-8


import scrapy
import json


class RenrenSpider(scrapy.Spider):
    name = "renren"
    # allowed_domains = ["renren.com"]
    start_urls = []

    def start_requests(self):
        """
            发送post请求，scrapy会保存登录状态的cookie
        """
        # post_url = "http://www.renren.com/PLogin.do"
        login_url_list = ['http://qd.pinganedai.vip/checkuser', 'https://saas.fin-tech.cn/admin/index.php?g=linkshare&m=index']
        for login_url in login_url_list:
            if login_url == 'http://qd.pinganedai.vip/checkuser':
                formdata = {
                    "username": "xlph01",
                    "password": "168703"
                }
                headers = {
                    'Cookie': 'JSESSIONID=C0F327043C632BE205F4AB87061D41BD; SERVERID=b2e64bcfc869f471689356521d14c788|1543742654|1543742555'
                }
                post_url = "http://qd.pinganedai.vip/website/csct/listSingleChannel"
                post_data = {
                    'page': '1',
                    'rows': '10',
                    'queryConditions.beginDate': '2018-12-02',
                    'queryConditions.endDate': '2018-12-02'
                }
                print('1111111')
            else:
                print('44444444')
                formdata = {
                    'username': 'huangzhenxia1',
                    'password' : '111111a'
                }
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
                }
                post_data = ''
                post_url = "https://saas.fin-tech.cn/admin/index.php/linkshare/index/share_count_ajax.html?page=1&limit=10&search_date_start=2018-12-01&search_date_end=2018-12-01"
            yield scrapy.FormRequest(login_url, meta={"post_url": post_url, "post_data": post_data}, formdata=formdata, headers=headers, callback=self.parse)

    def parse(self, response):
        """
            附带登录状态的cookie，发送其他页面的get请求，并调用回调函数解析数据
        """
        # self.logger(response.body.decode())
        post_url = response.meta["post_url"]
        post_data = response.meta["post_data"]
        print('2222222')
        yield scrapy.FormRequest(post_url, formdata=post_data, callback=self.parse_page)


    def parse_page(self, response):
        print(response.body.decode())
        print('33333333')
        item = {}
        register = json.loads(response.body.decode()).get('rows')[0].get('reg')
        item['register'] = register
        print(item)


