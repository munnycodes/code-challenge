from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
from pathlib import Path

html_file_name = 'van-gogh-paintings.html'

remote_prefix = 'https://www.google.com/'
local_protocol = 'file:///'

carousel_item_class_name = "iELo6"
title_class_name = "pgNMRc"
extension_class_name = "cxzHyb"
# image_class_name = "taFZJe"

options = FirefoxOptions() # setting object container
options.add_argument("--headless") # add a setting to the container
driver = webdriver.Firefox(options=options) # launching firefox with the settings passed in
absolute_file_path = f'{local_protocol}{Path('.', html_file_name).resolve()}'
driver.get(absolute_file_path)

carousel_web_elements = driver.find_elements(By.CLASS_NAME, carousel_item_class_name)

artworks_output = []

for carousel_element in carousel_web_elements:
    image_element = carousel_element.find_element(By.TAG_NAME, 'img')
    # Get the images that are lazily loaded
    src = image_element.get_attribute('data-src')
    if not src:
        # Get the images that are eagerly loaded
        src = image_element.get_attribute('src')

    title_element = carousel_element.find_element(By.CLASS_NAME, title_class_name)
    title = title_element.get_attribute('textContent')

    extension_element = carousel_element.find_element(By.CLASS_NAME, extension_class_name)
    extension = extension_element.get_attribute('textContent')

    link_element = carousel_element.find_element(By.TAG_NAME, 'a')
    link_suffix = link_element.get_attribute('href')

    output = {}
    if title:
        output["name"] = title
    if extension:
        output["extensions"] = [extension] if extension else []
    if link_suffix:
        raw_link = link_suffix.removeprefix(local_protocol)
        output["link"] = remote_prefix + raw_link
    if src:
        output["image"] = src
    artworks_output.append(output)

with open("actual-array.json", 'w') as f:
    json.dump({
        "artworks": artworks_output
    }, f, indent=2, ensure_ascii=False)