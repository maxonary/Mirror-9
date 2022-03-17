from cgitb import html
from re import S
from flask import Flask
import requests
import time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


"""Set language for translation"""
language = "german"


class Selenium_Weather_Test:

    """Selenium select webdriver"""
    def __init__(self):
        self.driver = webdriver.Chrome("/Users/maximilianarnold/Documents/Programmieren/Mirror-9/chromedriver")

    """Prevent E2E test from stoping due to loading issues and find by CSS path"""
    def awaitElement(self, selector):
        element = None

        while element == None:
            time.sleep(0.5)
            element = self.driver.find_element_by_css_selector(selector)
            print(element)

        return element

    """Open browser and translate"""
    def open_browser_translate(self, input_text):
        self.driver.maximize_window()
        self.driver.get("https://translate.google.com")

        #accept cookies
        time.sleep(1.5)
        agree_to_terms = self.driver.find_element_by_xpath("//*[contains(text(), 'Ich stimme zu')]")
        agree_to_terms.click()

        """Select input language = English"""
        english_button = None
        while not english_button:

            try:
                time.sleep(1)
                english_button = self.driver.find_element_by_xpath("//*[contains(text(), 'ENGLISCH')]")  
                english_button = self.driver.find_element_by_xpath('//button[text()="ENGLISCH"]')

            except NoSuchElementException:
                time.sleep(1)
                #select input dropdown menu
                input_language_menu = self.driver.find_element_by_css_selector("body > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.aCQag > c-wiz > div.zXU7Rb > c-wiz > div:nth-child(2) > button > div.VfPpkd-Bz112c-RLmnJb")
                input_language_menu.click()
                
                #select input language button
                try: 
                    english_button = self.driver.find_element_by_css_selector()
                except NoSuchElementException:
                    english_button = self.driver.find_elements_by_css_selector("#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.aCQag > c-wiz > div:nth-child(2) > c-wiz > div.OoYv6d > div > div.dykxn.MeCBDd.j33Gae > div > div:nth-child(3) > div:nth-child(19) > div.Llmcnf")
            
        english_button.click()

        '''#select input dropdown menu
        time.sleep(0.5)
        input_language_menu = self.driver.find_element_by_css_selector("body > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.aCQag > c-wiz > div.zXU7Rb > c-wiz > div:nth-child(2) > button > div.VfPpkd-Bz112c-RLmnJb")
        input_language_menu.click()

        #select input language button
        time.sleep(0.5)
        english_button = self.driver.find_element_by_xpath("//*[contains(text(), 'ENGLISCH')]")
        english_button.click()'''


        """Select output language = variable"""
        language_button = None
        while not language_button:
            try: 
                language_button = self.driver.find_element_by_xpath(f"//*[contains(text(), '{language.upper()}')]")

            except NoSuchElementException:
                time.sleep(0.5)
                #select output dropdown menu
                output_language_menu = self.driver.find_element_by_css_selector("#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.aCQag > c-wiz > div.zXU7Rb > c-wiz > div:nth-child(5) > button")
                output_language_menu.click()

                #select output language button
                #default = Filipino
                language_button = self.driver.find_element_by_css_selector("#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.aCQag > c-wiz > div:nth-child(2) > c-wiz > div.OoYv6d > div > div.dykxn.MeCBDd.j33Gae > div > div:nth-child(3) > div:nth-child(22)")

        language_button.click()

        '''#select output dropdown menu
        time.sleep(0.5)
        output_language_menu = self.driver.find_element_by_css_selector("#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.aCQag > c-wiz > div.zXU7Rb > c-wiz > div:nth-child(5) > button")
        output_language_menu.click()

        #select output language button
        time.sleep(0.5)
        german_button = self.driver.find_element_by_xpath(f"//*[contains(text(), '{language}')]")
        german_button.click()'''

        #paste weather text in input field
        input_field = self.awaitElement("#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea")
        input_field.clear()

        #input_field.send_keys(self.data["weather"][0]["description"])
        input_field.send_keys(input_text)

        #fetch translated text by copying with clipboard button and Pyperclip
        output_text = self.awaitElement("#ow251 > div > span > button > div.VfPpkd-Bz112c-RLmnJb").click()
        print(output_text)
        return output_text


    """Close Selenium browser"""
    def close_browser(self):
        self.driver.close()


app = Flask(__name__)

"""Main page on port 5000"""
@app.route("/")
def index():
    return "<p>Hello, World!</p>"

"""Receive json list and return new list"""
@app.route("/weather")
def weather_request():
    api_key = "87b984ab68a0c5ba314b0b1148ad540e"
    city = "berlin"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
    response = requests.get(url)

    data = response.json()

    city_data = {
        "city": data["name"],
        "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]),
        "sunset": datetime.fromtimestamp(data["sys"]["sunset"])
    }

    weather_data = {
        "city": data["name"],
        "weather": data["weather"][0]["description"],
        "temperature": round(kelvin_to_celsius(data["main"]["feels_like"]), 1)
    }

    translated_weather_data = {
        "translated_weather": Selenium_Weather_Test().open_browser_translate(data["weather"][0]["description"])
    }

    return {"city_data":city_data, "weather_data":weather_data, "translated_weather_data":translated_weather_data}

"""Convert Kelvin to Celsius"""
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

"""Automatically reload Flask when saved"""
if __name__ == '__main__':
    app.run(debug=True) #turn to "False" when leaving production