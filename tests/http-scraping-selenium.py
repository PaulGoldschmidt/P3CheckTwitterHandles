from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def is_handle_claimed(handle):
    # Replace this with the path to your WebDriver
    driver_path = "/path/to/your/webdriver"

    options = webdriver.ChromeOptions()
    # Uncomment the following line to run the browser in headless mode
    # options.add_argument('--headless')
    driver = webdriver.Chrome(driver_path, options=options)
    
    url = f"https://twitter.com/{handle}"
    driver.get(url)

    try:
        driver.find_element_by_css_selector("div[data-testid='primaryColumn'] h2")
        claimed = False
    except NoSuchElementException:
        claimed = True

    driver.quit()
    return claimed

handle = "example_handle"
if is_handle_claimed(handle):
    print(f"The handle @{handle} is claimed.")
else:
    print(f"The handle @{handle} is not claimed.")
