from lib_scraping import * 

def html_source_browser(negara,partner, browser2):
    browser = browser2
    

    # select = Select(WebDriverWait(browser, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//select[@id='ctl00_NavigationControl_DropDownList_Country']"))))
    # select.select_by_value(negara)
    # browser.implicitly_wait(20)

    # time.sleep(3)
    
    select = Select(WebDriverWait(browser,30).until(
        EC.element_to_be_clickable((By.XPATH, "//select[@id='ctl00_NavigationControl_DropDownList_Partner']"))))
    select.select_by_value(partner)
    browser.implicitly_wait(20)
    

    time.sleep(5)





 
    html_source = []
    html_source.append((browser.page_source))
    
    
    while True:

        try:
            WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//table[@id='ctl00_PageContent_MyGridView1']//table/tbody/tr//td/span//following::td[1]/a"))) 
            browser.find_element_by_xpath("//table[@id='ctl00_PageContent_MyGridView1']//table/tbody/tr//td/span//following::td[1]/a").click()
            browser.implicitly_wait(20)
            
            time.sleep(10)
            html_source.append((browser.page_source))
        except TimeoutException:
            break

 
    return html_source

def data_import_export_extract(html_source, angka ):
    soup = BeautifulSoup(html_source,'html.parser')
    global tdTags

    data = soup.findAll('td',{'class':['tabContent']})

    web = []
    for item in data:
        tdTags = item.find_all("tr")
    for item in tdTags:
        for asii in item.find_all("td") :
                #print(no , asii.text)
                #product_code.append(asii.text.strip())
            web.append(asii.text.strip())
    if angka != 1:
        web = web[15:]
    else :
        web = web[35:]


    return web

def insert_into_list(web):
    m = len(web)
    n = 20

    product_code = []
    product_label = []
    value_2016 = []
    value_2017 = []
    value_2018 = []
    value_2019 = []
    value_2020 = []

    for i in range(0, m, n):
        # print(web[i])
        product_code.append(web[i])
        product_label.append(web[i + 1])
        value_2016.append(web[i + 2])
        value_2017.append(web[i + 3])
        value_2018.append(web[i + 4])
        value_2019.append(web[i + 5])
        value_2020.append(web[i + 6])

    # make dataframe
    kolom = ['product_code', 'product_label', '2016', '2017', '2018', '2019', '2020']
    df = pd.DataFrame(columns=kolom)
    df['product_code'] = product_code
    df['product_label'] = product_label
    df['2016'] = value_2016
    df['2017'] = value_2017
    df['2018'] = value_2018
    df['2019'] = value_2019
    df['2020'] = value_2020
    return df

