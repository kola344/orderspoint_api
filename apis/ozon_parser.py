import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def parse_url(url):
    cookies = {
        '__Secure-refresh-token': '4.0.akpFuPb7StOlnEeV6bYcIw.37.AWvfIdyoSWCTlqloNJZkfg-1wwyHhh1cCv2iaj8IESu90DuA-z_fslyokCSgvJtJdg..20240613221546.CkTJua8oCvT5MOF3FW2c6qEV6ZbGAJLka7rIWehjX2o',
        'abt_data': 'b143305a8eaaf7009496b5d8a67b8552:07489a5629102710d12c86d9a7d4cb0d8c979cd38e57f5f694560ebef4c230cd182f941bde466dabb693bbf85a65ffff7888838bd356a0c8b5b4ded444dc7fdd21a09bc658df9a22ae1f6d2f81a65b8755927e8210207d6063b05d0d216bc3007c12bf7e9f3fa154cd8086fc852d7830aca8b48586f844aae9fbe88dbd89f82e2188cb125bbd35cda8e63b4db72e4a3768f65c8de488980b6c3bed4020f93bac1c8c71fa8d333e193cbcbb2dad0288494ee9fbd44ff78e4f3f9a6d277d7beb24bb4c0f504ac46b678db1c6a344b2f3e3d6fccdc551e6822dd67f80fc6c4d55351d2c5713cac6627ca16fe925baca4e6389525d88c57c4fd69ad1026da39fc9c8c57d064cc2bf40b5f66ed7d31c601d2506ff56be413af509f46dfb10d9c0030fd3b995b5a8a2ec0876d3be7c21fb6035',
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, cookies=cookies, ssl=False) as response:
            response_text = await response.text()
            soup = BeautifulSoup(response_text, 'html.parser')
            address = soup.find_all('span', class_='tsBody500Medium')
            grade = soup.find_all('div', class_="b21-b0 tsBodyControl300XSmall")

            return address[0].text, grade[0].text
