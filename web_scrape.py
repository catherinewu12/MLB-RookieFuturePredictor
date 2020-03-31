import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv('C:/Users/cat_w/Documents/Second Year/QSAO/project/Rookies2000-2014.csv')

df["five_years"] = 0

#get url for each diff player
def get_url(name, id):
    my_url = "https://www.fangraphs.com/players/" + str(name) + "/" + str(id)
   # print (my_url)
    return my_url


#call function to return player url based on names from csv
for i in range(len(df)):
    name = df["Name"][i].replace(' ', '-').lower()
    my_url = get_url(name, df["playerid"][i])

    try:
        # grab the HTML from the site
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        #Beautiful soup this thing
        soup = BeautifulSoup(page_html, "html.parser")
        #finding the years active

        try :
            text = soup.find("span", text="Service Time").find_next().text
            years = int(text[31:34])
            print (years)
            if years >= 5:
                df["five_years"][i] = 1
        except:
            print("didn't make it")
    except:
        df.to_csv(r'C:/Users/cat_w/Documents/Second Year/QSAO/project/newRookies2000-2014.csv')


#f["five_years"] = made_it
print(df["five_years"])
