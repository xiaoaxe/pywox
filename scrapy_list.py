# 爬取列表数据

import requests
from lxml import etree
import os
import sys
import time

two_foot = 'https://www.2bulu.com/track/track_search_result.htm'
data_fmt = 'key=&pageNumber={}&sortType=0&minMileage=&maxMileage=&trackType=&firstFindPageTime=&areaId=50&parentId=50'
host = 'https://www.2bulu.com/'


def scrapy():
    fw = open(os.environ['HOME']+'/Downloads/two_foot.csv', 'w')
    fw.write('name\turl\tdis\tvote\tdown\tfav\n')

    total = 0
    for i in range(1, 1001):
        for retry in range(3):
            resp = requests.post(
                two_foot, data=data_fmt.format(i), headers=headers)
            html = etree.HTML(resp.content.decode())

            items = html.xpath('//div[@class="guiji_discription"]')
            if len(items) == 0:
                print('sleeping: {}, retry: {}'.format(i, retry))
                sys.stdout.flush()
                time.sleep(5)
                # s = etree.tostring(html).decode()
                # print('err page: {}'.format(s))
                # sys.exit(-1)
            else:
                break

        total += len(items)
        for item in items:
            dic = {}
            names = item.xpath('.//p[@class="guiji_name"]/text()')
            url = item.xpath('./a/@href')
            dis = item.xpath('.//span[@class="s1"]/text()')
            vote = item.xpath('.//span[@class="s3"]/text()')
            dls = item.xpath('.//span[@class="s4"]/text()')
            fav = item.xpath('.//span[@class="s5"]/text()')

            # build dic
            dic['name'] = trim_space(names)
            dic['url'] = '{}{}'.format(host, ''.join(url))
            dic['dis'] = trim_space(dis)
            dic['vote'] = trim_text(vote)
            dic['dls'] = trim_text(dls)
            dic['fav'] = trim_text(fav)

            # write file
            fw.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(
                dic['name'], dic['url'], dic['dis'],
                dic['vote'], dic['dls'], dic['fav']))

        # only one
        # break
        if i % 10 == 0:
            print('process cnt: {}, current cnt: {}'.format(i, total))
            sys.stdout.flush()
            fw.flush()

        time.sleep(3)

    # close
    fw.close()


headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Referer': 'https://www.2bulu.com/track/list-----50-1.htm',
    'Connection': 'keep-alive',
    'Cookie': 'SECKEY_CID2=3ef0cf73bfab64f0683d299a86d3bee249449ad7; BMAP_SECKEY2=68929e83979a78fd015ed358fefc384ad77c1b324b8cc6f266f2a8ebe521879133a4ab1c7df9cb3c91dfbc5248943b06f8c7b7cc20a008330338202950984db991cecac3632434ff00e29d6c414bf91b6a68ed2edf415698af88a8d084205d969b6be5caef022a630bb1dc177c0c6a0268acd90c2b35f06275b3efbca3cdaabb036b7e13c370f55a2a95e6bcc25268dbdb62241b38871aa1de289b25966abee220f60b8004134cd970d91f64dbf45665086fa2df6b645aa283ed77002f5b9cc6c1c98ecf9b715dc070b2704ca7761ee42c478c31062faab65f89ca0c78529c46; UM_distinctid=17d36ab6c6d703-0dde26dcb360a3-1e396452-1fa400-17d36ab6c6ea93; JSESSIONID=A5A968AFFF629B7E4C45349EAC68DE82-n3; CNZZDATA1000341086=484427558-1637294121-https%253A%252F%252Fwww.google.com.hk%252F%7C1637315875',
}


def trim_text(datas):
    data = ''.join(datas)
    data = data.replace('赞', '').replace('下载', '').replace('收藏', '')
    return data.replace('(', '').replace(')', '')


def trim_space(datas):
    data = ''.join(datas)
    return data.replace('\n', '').replace('\t', '').replace(' ', '')


if __name__ == '__main__':
    scrapy()
