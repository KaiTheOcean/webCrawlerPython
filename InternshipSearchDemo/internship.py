import requests
from lxml import etree

headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

# Get the user inputs for search
area = input("Enter the area you'd like to search: (auto/web/software. etc) ")
title = input("Enter the title you'd like to search: (engineer/developer . etc ")
type = input("Enter the position you are looking for: (full-time/part-time/internship .etc) ")
year = input("Enter the year you are looking for this position? ")

url = (f"https://www.google.com/search?q={area}+{title}+{type}+{year}&ibp=htl;jobs&sa=X&ved=2ahUKEwiYl-TW_e_6AhUxHDQIHfyBD0oQutcGKAF6BAgKEAs&sxsrf=ALiCzsYpKdv0wUoGkIaoTjOuBwVYDKCNgA:1666309248591#htivrt=jobs&htidocid=0QvDr6JC73cAAAAAAAAAAA%3D%3D&fpstate=tldetail")

# Send requests
response = requests.get(url, headers = headers)

# Process the reuslt
e = etree.HTML(response.text)

# Internship Title
titles = e.xpath("//*[@id='immersive_desktop_root']/div/div[3]/div[1]/div/div/ul/li/div/div/div/div/div/div[2]/div[2]/text()")

# Gets all the company names 
names = e.xpath("//*[@id='immersive_desktop_root']/div/div[3]/div[1]/div/div/ul/li/div/div/div/div/div/div/div/div[1]/text()")

# Gets all the location
locations = e.xpath("//*[@id='immersive_desktop_root']/div/div[3]/div[1]/div/div/ul/li/div/div/div/div/div/div/div/div[2]/text()")

# Input a file name to store later
file = input("Type a file name to store the data: ")

# Save in the file
with open(f"{file}.csv", "w") as file:

    # Loop through the three items and print them individually
    for title, name, location in zip(titles, names, locations):
        file.write(f"Title: {title} || Company: {name} || Location: {location} \n")
