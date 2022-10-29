import requests 
from lxml import etree

url = "http://nba.hupu.com/stats/players/pts"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

response = requests.get(url, headers = headers) # Send request

# 处理结果
e = etree.HTML(response.text)


# 解析响应的数据
numbers = e.xpath('//table[@class="players_table"]//tr/td[1]/text()') # Get their number
names = e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()') # Get the player names
teams = e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()') # Get the team names

# # Save in the file
# with open("nbaPlayerInfo.txt", "w", encoding="utf-8") as file:

#     # Loop through the three items and print them individually
#     for number, name, team in zip(numbers, names, teams):
#         file.write(f"Order: {number} Name: {name} Team: {team}\n")
