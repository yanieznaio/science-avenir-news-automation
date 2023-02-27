from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys


application_path = os.path.dirname(sys.executable)
now = datetime.now()
month_day_year = now.strftime("%m%d%y")


website = "https://www.sciencesetavenir.fr/"
path = "C:\\Dev\\WebDriver\\chromedriver_win32\\chromedriver.exe"

## lance chromedriver
## la page web ne sera pas afficher sur l'écran avec l'option headless
options = Options()
options.add_argument('--headless')
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)


# trouver le container parent des élements qui nous intéresse
# trouver les élements qui nous interésse sur la page science avenir
# ajouter les titres des articles et les liens dans les tableaux correspondant
containers = driver.find_elements(by="xpath", value='//div[@class="more"]/div')

titles = []
links = []


for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    links.append(link)



my_dict = {'title': titles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
#créer le fichier avec la date du jour
file_name = f'headline-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)

driver.quit()

