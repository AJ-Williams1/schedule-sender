from bs4 import BeautifulSoup
import re

daysdict = {}

def parse_html():
    with open("cal.html", "r+") as f:
        soup = BeautifulSoup(f, 'html.parser')

    tables = soup.find_all("table")

    rows = []
    days_children = []
    days = []
    weekdaynames = [re.compile(".*Monday.*"), re.compile(".*Tuesday.*"), re.compile(".*Wednesday.*"), re.compile(".*Thursday.*"), re.compile(".*Friday.*")]


    for table in tables:
        rows.append(table.find("tr"))

    for row in rows:
        days_children.extend(row.find_all("span", string=weekdaynames))

    for day_child in days_children:
        days.append(day_child.find_parent().find_parent())
    
    for day in days:
        if(goodday := day.find("span", string=re.compile("\w+\ \d{1,2},\ \d{4}"))):
            if(goodday.find_parent().find_parent().find("span", string=re.compile(".*Day\ \d.*"))):
                daysdict[goodday.get_text().strip()] = goodday.find_parent().find_parent().find("span", string=re.compile(".*Day\ \d.*")).get_text().strip()

def get_day(datestring):
    parse_html()
    daytext = daysdict[datestring]
    return int(re.search("\d", daytext).group())