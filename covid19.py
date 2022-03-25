from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup as BS


class COVID19:
    """
    COVID-19 butun dunyo satitstikasini olish uchun


    ```python
    covid19 = COVID19()
    print(covid19)
    ```
    """

    def __init__(self):
        self.url = 'https://www.worldometers.info/coronavirus/'
        self.response = requests.get(self.url)
        self.soup = BS(self.response.text, 'html.parser')
        self.data = self.soup.find_all('div', class_='maincounter-number')
        self.confirmed = self.data[0].text.strip()
        self.deaths = self.data[1].text.strip()
        self.recovered = self.data[2].text.strip()
        self.active = self.confirmed.split(' ')[0]
        self.death_rate = self.deaths.split(' ')[0]
        self.recovery_rate = self.recovered.split(' ')[0]
        self.active_rate = self.active.split(' ')[0]

    def __str__(self):
        return f'Confirmed: {self.confirmed}\nDeaths: {self.deaths}\nRecovered: {self.recovered}\nActive: {self.active}\nDeath Rate: {self.death_rate}\nRecovery Rate: {self.recovery_rate}\nActive Rate: {self.active_rate}'

    def country(self, country):
        """
        Davlat uchun satitstikasini olish uchun

        ```python
        covid19 = COVID19()
        print(covid19.country('uzbekistan'))
        ```
        """
        self.url = f'https://www.worldometers.info/coronavirus/country/{country}/'
        self.response = requests.get(self.url)
        self.soup = BS(self.response.text, 'html.parser')
        self.data = self.soup.find_all('div', class_='maincounter-number')
        self.confirmed = self.data[0].text.strip()
        self.deaths = self.data[1].text.strip()
        self.recovered = self.data[2].text.strip()
        self.active = self.confirmed.split(' ')[0]
        self.death_rate = self.deaths.split(' ')[0]
        self.recovery_rate = self.recovered.split(' ')[0]
        self.active_rate = self.active.split(' ')[0]
        return f'Confirmed: {self.confirmed}\nDeaths: {self.deaths}\nRecovered: {self.recovered}\nActive: {self.active}\nDeath Rate: {self.death_rate}\nRecovery Rate: {self.recovery_rate}\nActive Rate: {self.active_rate}'

    def get_total_deaths(self):
        """
        Butun dunyoda o'limlar

        ```python
        covid19 = COVID19()
        print(covid19.get_total_deaths())
        ```
        """
        return self.deaths

    def get_total_recovered(self):
        """
        Butun dunyoda tuzalganlar

        ```python
        covid19 = COVID19()
        print(covid19.get_total_recovered())
        ```
        """
        return self.recovered

    def get_total_confirmed(self):
        """
        Butun dunyoda kasallanganlar

        ```python
        covid19 = COVID19()
        print(covid19.get_total_confirmed())
        ```
        """
        return self.confirmed

    def get_total_active(self):
        """
        Butun dunyoda faoliyatlar

        ```python
        covid19 = COVID19()
        print(covid19.get_total_active())
        ```
        """
        return self.active
