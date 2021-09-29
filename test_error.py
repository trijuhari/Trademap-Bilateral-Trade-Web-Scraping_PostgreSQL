from lib_scraping import * 
from connect_db import  *

from scrape_data  import * 

def main(): 
	# options = FirefoxOptions()
	# options.add_argument("--headless")
	browser = webdriver.Firefox(  )
	executor_url = browser.command_executor._url
	session_id = browser.session_id
	browser.get(f"https://www.trademap.org/Bilateral_TS.aspx?nvpm=1|360||004||TOTAL|||2|1|1|2|2|1|1|1|1|1")
	 
	
	select = Select(WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
	    (By.XPATH, "//select[@id='ctl00_PageContent_GridViewPanelControl_DropDownList_NumTimePeriod']"))))
	select.select_by_value('5')

	time.sleep(5)
	 
	select = Select(WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
	    (By.XPATH, "//select[@id='ctl00_NavigationControl_DropDownList_ProductClusterLevel']"))))
	select.select_by_value('4')

	
	time.sleep(5)

	select = Select(WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
	    (By.XPATH, "//select[@id='ctl00_PageContent_GridViewPanelControl_DropDownList_PageSize']"))))
	select.select_by_value('300')

 
	print (session_id)
	print (executor_url)

	def create_driver_session(session_id, executor_url):
	    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

	    # Save the original function, so we can revert our patch
	    org_command_execute = RemoteWebDriver.execute

	    def new_command_execute(self, command, params=None):
	        if command == "newSession":
	            # Mock the response
	            return {'success': 0, 'value': None, 'sessionId': session_id}
	        else:
	            return org_command_execute(self, command, params)

	    # Patch the function before creating the driver object
	    RemoteWebDriver.execute = new_command_execute

	    new_browser = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
	    new_browser.session_id = session_id

	    # Replace the patched function with original function
	    RemoteWebDriver.execute = org_command_execute

	    return new_browser

	browser2 = create_driver_session(session_id, executor_url)




	con, kode_negara, kombinasi_negara =  get_code_country(connect_db)


	no =[x for x in range(20, 300,20)]
	kombinasi_negara = ['052',
 '112',
 '056',
 '084',
 '204',
 '060',
 '064',
 '074',
 '080',
 '192',
 '208',
 '214',
 '226',
 '231',
 '568',
 '238',
 '838',
 '288',
 '300',
 '304',
 '324',
 '340',
 '360',
 '381',
 '388',
 '440',
 '442',
 '454',
 '458',
 '470',
 '584',
 '480',
 '175',
 '583',
 '662']
​
	for i,kombinasi in enumerate(kombinasi_negara,1):
		kolom = ['product_code', 'product_label', '2016', '2017', '2018', '2019', '2020','importer','exporter']
		data_exportir = pd.DataFrame(columns=kolom)

		if  i>= 0 and  i <= len(kombinasi_negara) and i  not in no :
			print(f"{i}/{len(kombinasi_negara)} Started")
			partner = kombinasi
			nama_negara = kode_negara['360']
			nama_partner = kode_negara[partner]
			html_source =  html_source_browser('360', partner, browser2)
			for i, data in  enumerate(html_source,1):
				web = data_import_export_extract(data,i)
				df = insert_into_list(web)
				df['importer'] = nama_partner  
				df['exporter'] = nama_negara
				df = df[df.product_code != "1" ]
				df = df[~df.duplicated()]
				data_exportir = pd.concat([df, data_exportir], axis = 0)
			if len (data_exportir) == 1225:
				data_exportir.to_sql('trademap_export_raw', con=con, if_exists='append')
			else:
				data_exportir.to_sql('trademap_wrongs', con=con, if_exists='append')


		elif  i>= 0 and  i <= len(kombinasi_negara) and i   in no :
			browser = webdriver.Firefox(  )
			executor_url = browser.command_executor._url
			session_id = browser.session_id
			browser.get(f"https://www.trademap.org/Bilateral_TS.aspx?nvpm=1|360||004||TOTAL|||2|1|1|2|2|1|1|1|1|1")
			 
			
			select = Select(WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
			    (By.XPATH, "//select[@id='ctl00_PageContent_GridViewPanelControl_DropDownList_NumTimePeriod']"))))
			select.select_by_value('5')

			time.sleep(5)
			 
			select = Select(WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
			    (By.XPATH, "//select[@id='ctl00_NavigationControl_DropDownList_ProductClusterLevel']"))))
			select.select_by_value('4')

			
			time.sleep(5)

			select = Select(WebDriverWait(browser, 20).until(EC.element_to_be_clickable(
			    (By.XPATH, "//select[@id='ctl00_PageContent_GridViewPanelControl_DropDownList_PageSize']"))))
			select.select_by_value('300')

		 
			print (session_id)
			print (executor_url)

			def create_driver_session(session_id, executor_url):
			    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

			    # Save the original function, so we can revert our patch
			    org_command_execute = RemoteWebDriver.execute

			    def new_command_execute(self, command, params=None):
			        if command == "newSession":
			            # Mock the response
			            return {'success': 0, 'value': None, 'sessionId': session_id}
			        else:
			            return org_command_execute(self, command, params)

			    # Patch the function before creating the driver object
			    RemoteWebDriver.execute = new_command_execute

			    new_browser = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
			    new_browser.session_id = session_id

			    # Replace the patched function with original function
			    RemoteWebDriver.execute = org_command_execute

			    return new_browser

			browser2 = create_driver_session(session_id, executor_url)


			print(f"{i}/{len(kombinasi_negara)} Started")
			partner = kombinasi
			nama_negara = kode_negara['360']
			nama_partner = kode_negara[partner]
			print(nama_partner)
			html_source =  html_source_browser('360', partner, browser2)
			for i, data in  enumerate(html_source,1):
				web = data_import_export_extract(data,i)
				df = insert_into_list(web)
				df['importer'] = nama_negara  
				df['exporter'] = nama_partner
				df = df[df.product_code != "1" ]
				df = df[~df.duplicated()]
				data_exportir = pd.concat([df, data_exportir], axis = 0)
			
				
			if len(data_exportir) == 1225:
				data_exportir.to_sql('trademap_export_raw', con=con, if_exists='append')
			else:
				data_exportir.to_sql('trademap_wrongs', con=con, if_exists='append')





	                
if __name__ == '__main__':
	main()


