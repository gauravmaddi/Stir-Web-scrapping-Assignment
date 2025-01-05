from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time

load_dotenv()



def fetch_trends(proxy_ip_port):
    

    # Configure Chrome Options
    options = webdriver.ChromeOptions()
    # options.add_argument(f'--proxy-server=http://{proxy_ip_port}')
    options.add_argument('--disable-blink-features=AutomationControlled')

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        # Check IP Address
        driver.get("https://api.ipify.org/?format=text")
        current_ip = driver.find_element(By.TAG_NAME, "body").text
        print(f"Current IP: {current_ip}")

        # Navigate to the Login Page
        driver.get("https://x.com/i/flow/login")
        
        # Explicit wait for the username field
        wait = WebDriverWait(driver, 15)
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "text")))
        username_field.send_keys(os.getenv("TWITTER_USERNAME")) 
        username_field.send_keys(Keys.RETURN)
        
        # Explicit wait for the password field
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.send_keys(os.getenv("TWITTER_PASSWORD"))  
        password_field.send_keys(Keys.RETURN)
        
        # Wait for login to complete
        time.sleep(10)
            
            # Locate "Trending now" section
        trends_section = driver.find_element(By.XPATH, '//h1[text()="Trending now"]/ancestor::section')
        
        # Fetch trends within the section
        trends = trends_section.find_elements(By.XPATH, './/div[@data-testid="trend"]')
        
        
        # # Extract the text for each trend
        top_trends = []
        for trend in trends[:4]:  
            trend_text = trend.text.split('\n')[1]  # Extract the trend title
            top_trends.append(trend_text)
            # print(trend.text)
        
        print("Top Trends:")
        for i, trend in enumerate(top_trends, 1):
            print(f"{i}. {trend}")
            
        print(f"Total trends fetched: {len(trends)}")
        for trend in trends:
            print(trend.text)
    
       
        
        return top_trends, current_ip

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
