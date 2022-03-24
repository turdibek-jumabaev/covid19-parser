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
        self.country_url = f'https://www.worldometers.info/coronavirus/country/{country}/'
        self.country_response = requests.get(self.country_url)
        self.country_soup = BS(self.country_response.text, 'html.parser')
        self.country_data = self.country_soup.find_all(
            'div', class_='maincounter-number')
        self.country_confirmed = self.country_data[0].text.strip()
        self.country_deaths = self.country_data[1].text.strip()
        self.country_recovered = self.country_data[2].text.strip()
        self.country_active = self.country_confirmed.split(' ')[0]
        self.country_death_rate = self.country_deaths.split(' ')[0]
        self.country_recovery_rate = self.country_recovered.split(' ')[0]
        self.country_active_rate = self.country_active.split(' ')[0]
        return f'Confirmed: {self.country_confirmed}\nDeaths: {self.country_deaths}\nRecovered: {self.country_recovered}\nActive: {self.country_active}\nDeath Rate: {self.country_death_rate}\nRecovery Rate: {self.country_recovery_rate}\nActive Rate: {self.country_active_rate}'
