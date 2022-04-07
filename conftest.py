#import pytest

# @pytest.yield_fixture(scope='session')
# def browser():
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

from selenium import webdriver
import pytest
import os
driver = None

'''
def pytest_runtest_setup(item):
    print
    print("\n######################\n setting up\n######################\n", item)
'''

def removeExtensionFile(filePath, fileExtension):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            if file.name.endswith(fileExtension):
                os.remove(file.path)
        return "Removed file: " + fileExtension
    else:
        return "Directory not found"

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    
    #To get current path
    cur_path = os.getcwd()
    #print("\n"+ cur_path)

    #To set report result path from current path
    report_path = os.path.join(cur_path, "resultreport\\")  

    #To add path as html code
    #path_for_html = report_path.replace("\\", "/")
    
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(report_path, file_name)
            if file_name:
            #############################################################################
            # Case 1. An absolute path at the point of PC code is running. It will be only availalbe at the PC.
            #############################################################################
            #    html = '<div><img src="file:/' + path_for_html + '%s" alt="screenshot" style="width:600px;height:228px;" ' \
            #           'onclick="window.open(this.src)" align="right"/></div>'%file_name
            #############################################################################
            # Case 2. A relative path which is available for all states. 
            #############################################################################
                html = '<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra



def _capture_screenshot(path, file_name):
    #D:\pythonproject\cvelist_scanauto\resultreport
    driver.get_screenshot_as_file(path + file_name)



@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver

    #To remove files except folder included
    cur_path = os.getcwd()

    report_path = os.path.join(cur_path, "resultreport\\")

    removeExtensionFile(report_path, ".PNG".lower())

    if driver is None:
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
    yield driver
    driver.quit()
    #driver.close()
    return driver