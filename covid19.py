import requests
from bs4 import BeautifulSoup as BS


class COVID19:
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
