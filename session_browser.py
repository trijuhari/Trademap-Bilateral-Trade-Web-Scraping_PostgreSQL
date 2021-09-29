
browser = webdriver.Firefox()
executor_url = browser.command_executor._url
session_id = browser.session_id
browser.get(f"https://www.trademap.org/Bilateral_TS.aspx?nvpm=1|360||004||TOTAL|||2|1|1|1|2|1|1|1|1|1")
 
time.sleep(3)
 
select = Select(WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//select[@id='ctl00_NavigationControl_DropDownList_ProductClusterLevel']"))))
select.select_by_value('4')
time.sleep(3)

select = Select(WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//select[@id='ctl00_PageContent_GridViewPanelControl_DropDownList_NumTimePeriod']"))))
select.select_by_value('5')
time.sleep(3)

select = Select(WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//select[@id='ctl00_PageContent_GridViewPanelControl_DropDownList_PageSize']"))))
select.select_by_value('300')
time.sleep(5)


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
