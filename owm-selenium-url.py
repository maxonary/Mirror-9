from cgitb import html
from re import S
from flask import Flask
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


"""Set language for translation"""
language = "german"

#get ISO_639 language codes
url = "https://gist.githubusercontent.com/carlopires/1262033/raw/c52ef0f7ce4f58108619508308372edd8d0bd518/gistfile1.txt"
response = requests.get(url)
iso_1 = response
print(type(iso_1))

#language.capitalize()
#print(iso_1.iso_639_choices['ab', 'Abkhaz'])

tl = "en"
#sl = iso_1language.capitalize()

#"city": data["name"]