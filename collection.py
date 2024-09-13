#pip install bs4
#pip install pandas
from bs4 import BeautifulSoup
import os
import pandas as pd
d={'title':[], 'price':[], 'link':[], 'image':[]}
for file in os.listdir("data"):
    try:
        with open(f"data/{file}", encoding='utf-8') as f:
            html_doc=f.read()
            
        soup=BeautifulSoup(html_doc, 'html.parser')

        #a_tag = soup.find('a') Both can be used
        a_tag = soup.find('div', class_='RfADt').find('a')
        # Extract the href attribute
        
        href = a_tag.get('href') if a_tag else None
        link="https:"+href
        title = soup.find('div', class_='RfADt').find('a').get('title')

        #to find the price
        price_tag = soup.find("span", attrs={"class":'ooOxS'})
        price=price_tag.get_text()

        #to extract the image
        img=soup.find('div', class_='picture-wrapper jBwCF').find('img').get('src')
    

        #Storing in Dictionary
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
        d['image'].append(img)
    except Exception as e:
        print(e)
    
df=pd.DataFrame(data=d)
df.to_csv("data.csv")    

   