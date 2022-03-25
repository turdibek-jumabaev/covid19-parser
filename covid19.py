from unittest import result
import requests
from bs4 import BeautifulSoup as BS
from typer import Typer


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
        result = dict()
        result['confirmed'] = self.confirmed
        result['deaths'] = self.deaths
        result['recovered'] = self.recovered
        result['active'] = self.active
        result['death_rate'] = self.death_rate
        result['recovery_rate'] = self.recovery_rate
        result['active_rate'] = self.active_rate
        return str(result)

    def country(self, country: str = "uzbekistan"):
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

    def get_total_death_rate(self):
        """
        Butun dunyoda o'limlar to'plami

        ```python
        covid19 = COVID19()
        print(covid19.get_total_death_rate())
        ```
        """
        return self.death_rate

    def get_total_recovery_rate(self):
        """
        Butun dunyoda tuzalganlar to'plami

        ```python
        covid19 = COVID19()
        print(covid19.get_total_recovery_rate())
        ```
        """
        return self.recovery_rate

    def get_total_active_rate(self):
        """
        Butun dunyoda faoliyatlar to'plami

        ```python
        covid19 = COVID19()
        print(covid19.get_total_active_rate())
        ```
        """
        return self.active_rate

    def get_total_death_rate_per_million(self):
        """
        Butun dunyoda o'limlar to'plami milliyoqdur

        ```python
        covid19 = COVID19()
        print(covid19.get_total_death_rate_per_million())
        ```
        """
        return self.death_rate
