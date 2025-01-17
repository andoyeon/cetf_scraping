from selenium import webdriver
import pandas as pd
from scrap.file_pk import read_file
from scrap.file_pk import save_file
from bs4 import BeautifulSoup
import time
from multiprocessing import Pool
from datetime import datetime



def scraping_output_02(keyword):

    # Chrome Option 설정하기
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # Chrome Driver 생성
    driver = webdriver.Chrome('C:\dev\chromedriver.exe', options=options)


    # 인증번호 사이트 접속
    driver.get('http://ecolife.me.go.kr/ecolife/slfsfcfst/index')

    try:
        # 검색창에 키워드 입력
        driver.find_element_by_name('srchWrd').send_keys(keyword)
        driver.find_element_by_class_name('btns').click()

        # 상단 제품 클릭
        prd = driver.find_element_by_xpath('//*[@id="printArea"]/table/tbody/tr[1]')
        prd.click()
        # //*[@id="printArea"]/table/tbody/tr[1]

        # 페이지에서 요소 추출
        # 요청 생성
        request = driver.page_source

        # 웨이팅 시간 추가
        # driver.implicitly_wait(20)

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(request, 'html5lib')
        # regs_date = soup.select('/*[@id="printArea"]/div[1]/table[1]/tbody/tr[3]/td')
        # regs_date = soup.select('#printArea')

        # time.sleep(1)

        data = soup.find('table', class_="inTbTy1").find_all('td')[2]
        date = str(data)[4:14]
        regs_dt = datetime.strptime(date, '%Y-%m-%d')

        return regs_dt
        # driver.implicitly_wait(20)
    except:
        date = '0000-00-00'
        regs_dt = datetime.strptime(date, '%Y-%m-%d')
        print('타임아웃 [{}] Error Existing...')
        # Chrome Driver 종료
    driver.close()



def html_scraping():
    regs_nms, regs_nums = read_file('product_list.csv')
    regs_dts = []
    for count in range(len(regs_nums)):
        regs_nm = regs_nms[count]
        regs_num = regs_nums[count]

        # 인증날짜 리스트 생성
        regs_dt = scraping_output_02(regs_num)
        regs_dts.append(regs_dt)

        print('=== [{}] {}, {}, {} ==='.format(count + 1, regs_nm, regs_num, regs_dt))
        if count % 10 == 0:
            print('--- %s seconds ---' % (time.time() - start_time))

    return count+1, regs_nm, regs_num, regs_dt





if __name__ == '__main__':
    start_time = time.time()
    print('Start:', start_time)

    regs_nm, regs_num, regs_dt = html_scraping()
    save_file(regs_nm, regs_num, regs_dt)
