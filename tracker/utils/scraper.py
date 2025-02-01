import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.options import Options

def scrape_product_price(url):
    try:
        # Configure Safari options
        safari_options = Options()
        safari_options.headless = True  # Run in background

        # Initialize Safari WebDriver
        driver = webdriver.Safari(options=safari_options)

        # Fetch the webpage
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Scrape price based on the website
        if "amazon" in url:
            try:
                # Find the price element using the class "a-offscreen"
                price_element = driver.find_element(By.CLASS_NAME, "a-offscreen")
                if price_element:
                    # Extract the price text (e.g., "$49.99")
                    price_text = price_element.get_attribute("textContent").strip()
                    # Remove the dollar sign and convert to float
                    price = float(price_text.replace("$", "").replace(",", ""))
                    driver.quit()
                    return price
                else:
                    print("Price element not found in Amazon page.")
                    driver.quit()
                    return None
            except Exception as e:
                print(f"Error finding price element: {e}")
                driver.quit()
                return None

        elif "walmart" in url:
            # Walmart price scraping (using Selenium)
            try:
                price_element = driver.find_element(By.CLASS_NAME, "price-characteristic")
                if price_element:
                    price = price_element.get_attribute("content")
                    driver.quit()
                    return float(price)
                else:
                    print("Price element not found in Walmart page.")
                    driver.quit()
                    return None
            except Exception as e:
                print(f"Error finding price element: {e}")
                driver.quit()
                return None

        elif "ebay" in url:
            # eBay price scraping (using Selenium)
            try:
                price_element = driver.find_element(By.CLASS_NAME, "ux-textspans")
                if price_element:
                    price = price_element.text.strip().replace("$", "").replace(",", "")
                    driver.quit()
                    return float(price)
                else:
                    print("Price element not found in eBay page.")
                    driver.quit()
                    return None
            except Exception as e:
                print(f"Error finding price element: {e}")
                driver.quit()
                return None

        else:
            print(f"Unsupported website: {url}")
            driver.quit()
            return None

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        if 'driver' in locals():  # Ensure driver is defined before quitting
            driver.quit()
        return None