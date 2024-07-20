from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

class WebDriver:
    
  location_data = {}
  
  def __init__(self):
    self.service = webdriver.ChromeService()
    self.options = Options()
    # self.options.add_argument('--headless')
    self.driver = webdriver.Chrome(service=self.service, options=self.options)
    self.driver.maximize_window()

    self.location_data["Reviews"] = []
  
  def scroll_the_page(self):
    try:
      start_time = time.time()

      pause_time = 3  # Waiting time after each scroll.
      max_stable_height = 9  # Number of consecutive height checks with no change to stop scrolling.
      stable_height_count = 0  # Counter for consecutive stable height checks.
      reached_page_end = False
      
      # Get initial height.
      last_height = self.driver.execute_script("return document.querySelector('div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde').scrollHeight")

      while not reached_page_end and stable_height_count < max_stable_height:
        scrollable_div = self.driver.find_element(By.CSS_SELECTOR, "div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde")  # Section of the scroll bar.
        scrollable_div.send_keys(Keys.END)  # Scroll to the bottom.

        time.sleep(pause_time)

        new_height = self.driver.execute_script("return document.querySelector('div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde').scrollHeight")
        
        if last_height == new_height:
          stable_height_count += 1
        else:
          last_height = new_height
          stable_height_count = 0  # Reset the counter if height changes.

      end_time = time.time()
      scroll_time = end_time - start_time
      print("Scroll time:", scroll_time)

      scrollable_div.send_keys(Keys.HOME) # Scroll the page back to the top.

    except Exception as e:
        print("An error occurred:", e)
  
  def delete_no_reviews(self):
    try:
      print("Delete no reviews")

      parent = self.driver.find_elements(By.CSS_SELECTOR, "div.jftiEf.fontBodyMedium")

      for p in parent:
        try:
          review = p.find_element(By.CLASS_NAME, "MyEned")

        except NoSuchElementException:
          self.driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", p)

    except Exception as e:
      print("An error DNR", e)
  
  def expand_all_reviews(self):
    try:
      print("Expand all reviews")

      element = self.driver.find_elements(By.CSS_SELECTOR, "button.w8nwRe.kyuRq")
      
      for i in element:
        i.click()

    except Exception as e:
      print("An error EAR", e)
  
  def get_reviews_data(self):
    try:
      print("Get reviews data")

      review_names = self.driver.find_elements(By.CLASS_NAME, 'd4r55') # List of the reviewer name.
      review_status = self.driver.find_elements(By.CLASS_NAME, 'RfnDt') # List of the reviewer status.
      review_dates = self.driver.find_elements(By.CLASS_NAME, 'rsqaWe') # List of the reviewer reviewed date.
      review_stars = self.driver.find_elements(By.CLASS_NAME, 'kvMYJc') # List of the reviewer rating.
      review_text = self.driver.find_elements(By.CLASS_NAME, 'wiI7pd') # List of the reviewer reviews.

      review_stars_final = []
      for i in review_stars:
        review_stars_final.append(i.get_attribute("aria-label"))

      review_text_final = []
      for i in review_text:
        review_text_final.append(i.text.replace('\n', ' '))

      review_names_list = [a.text for a in review_names]
      review_status_list = [a.text for a in review_status]
      review_dates_list = [a.text for a in review_dates]
      review_stars_list = [a for a in review_stars_final]
      review_text_list = [a for a in review_text_final]

      for (a,b,c,d,e) in zip(review_names_list, review_status_list, review_dates_list, review_stars_list, review_text_list):
        self.location_data["Reviews"].append({"name":a, "status":b, "date":c, "rating":d, "review":e})

    except Exception as e:
      print("An error GRD", e)

  def scrape(self, url): # Passed the URL as a variable.
    try:
      self.driver.get(url) # Get is a method that will tell the driver to open at that particular URL.

    except:
      self.driver.quit()
      return

    time.sleep(5) # Waiting for the page to load.

    self.scroll_the_page() # Scroll the page to the bottom.
    self.delete_no_reviews()
    self.expand_all_reviews() # Expanding the long reviews by clicking see more button in each review.
    self.get_reviews_data() # Getting all the reviews data.

    self.driver.quit() # Closing the driver instance.

    # export dataset
    df = pd.DataFrame(data=self.location_data["Reviews"])
    df.to_csv("Puntikayu.csv")

    return(self.location_data) # Returning the Scraped Data.

start_time = time.time()

x = WebDriver()
url = "https://www.google.com/maps/place/Taman+Wisata+Alam+Punti+Kayu/@-2.9437208,104.7256982,17z/data=!4m8!3m7!1s0x2e3b74795c704869:0x30e21e94d2770c6!8m2!3d-2.9437262!4d104.7282731!9m1!1b1!16s%2Fg%2F122d8c2g?hl=id&entry=ttu"
print(x.scrape(url))

end_time = time.time()
execution_time = start_time - end_time
print("Execution time:",execution_time)