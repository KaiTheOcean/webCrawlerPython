# Crawler: Through code to find information on the internet
# Demand: Use prgram to replace browser, type a website and find information on that website

from urllib.request import urlopen 

url = "https://byui.joinhandshake.com/stu" # Pass the website into a variable
response = urlopen(url) 

# print(response.read().decode("utf-8")) # Allows us to read the information from (url) and then decode it

with open("byuiHandshake.html", mode="w") as file:
    file.write(response.read().decode("utf-8")) # Read the webpage's source code
print("It's done")