# selenium: 自动化检测工具
# 可以打开浏览器 然后像人一样去操作浏览器
# 程序员可以从selemium中直接提取网页上的信息
# 环境搭建： pip install selenium
# 下载浏览器驱动 https://npm.taobao.org/mirrors/chromedriver

# 让selenium启动浏览器
from selenium.webdriver import Chrome

# Make the web variable
web = Chrome() 

# Open a website
web.get("https://chromedriver.chromium.org/downloads") 

print(web.title)