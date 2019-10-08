from selenium import webdriver
from selenium.webdriver.common.keys import Keys

query = input("Google search: ")

driver = webdriver.Chrome()
driver.get("http://www.google.com/shopping")

search = driver.find_element_by_xpath("/html/body/gx-app/div[1]/gx-navigation-bar-ce/header/div/div[2]/gx-search-bar/div/form/div/input")
search.send_keys(query)
search.submit()

results = {}
products = driver.find_elements_by_class_name("sh-dgr__grid-result")
for element in products:
    price = element.find_element_by_class_name("Nr22bf").text
    results[element.find_element_by_class_name("EI11Pd").text] = float(price[1:len(price)-1])

sortedResults = {}
while len(results.keys()) > 0:
    min = 1000000
    key = ""
    for i in results:
        if results[i] < min:
            min = results[i]
            key = i
    sortedResults[key] = min
    del results[key]
    
for element in sortedResults:
    print(element, "\t", sortedResults[element])

