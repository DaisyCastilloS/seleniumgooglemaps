

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

#bajar el driver de la version del navegador y colocarlo en la ruta del rpyecto o en local)
s =Service("/usr/local/bin/chromedriver")
driver= webdriver.Chrome(service=s)
driver.get("https://www.google.com/maps/@-33.3891815,-70.6335762,15z")
sleep(2)

#para que funcione,debemos buscar una ubicacion en google maps.eso se configura asi:
# uno se posiciona en la barra de busqueda de google maps e inspecciona elemento
#una vez seleccionado eso en el DOM,se copia la ryuta path a este archivo
def searchplace():
    Place = driver.find_element_by_class_name("tactile-searchbox-input")
    Place.send_keys("Santiago")
    Submit = driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button"
    )
    Submit.click()


searchplace()


def directions():
    sleep(10)
    directions = driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button"
    )
    directions.click()


directions()


def find():
    sleep(6)
    find = driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input"
    )
    find.send_keys("Antofagasta")
    sleep(2)
    search = driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]"
    )
    search.click()


find()


def kilometers():
    sleep(5)
    Totalkilometers = driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div[1]/div/div[1]/div[1]/div[2]/div"
    )
    print("Total Kilometers:", Totalkilometers.text)
    sleep(5)
    Bus = driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div[1]/div/div[1]/div[1]/div[1]/span[1]"
    )
    print("Bus Travel:", Bus.text)
    sleep(7)
    Automovil = driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div[1]/div/div[1]/div[1]/div[1]/span[1]"
    )
    print("Automovil Travel:", Automovil.text)
    sleep(7)
    Avion = driver.find_element_by_xpath(
        "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[8]/div[3]/div/div[4]/div[1]/div/div[1]"
    )
    print("Avion Travel:", Avion.text)
    sleep(7)

kilometers()


def available():
    print("*COVID-19 Special Trains*")
    sleep(7)
    trainone = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[2]/span/span[2]/span[1]/span[1]/span"
    )
    print("Train No:1", trainone.text)


def availableone():
    trainsec = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[2]/span/span[8]/span[1]/span[1]/span"
    )
    print("Train No:2", trainsec.text)


available()
availableone()
