from urllib.request import urlopen as ureq
from urllib import error as urlerr
from bs4 import BeautifulSoup as soup
import sys
from opts import getOpts

options = getOpts(sys.argv[1:])

cities = [
    options.ljubljana, 
    options.novomesto, 
    options.maribor, 
    options.murska_sobota,
    options.nova_gorica,
    options.portoroz
]

urls = {
    options.ljubljana     : "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_LJUBL-ANA_BEZIGRAD_history.html",
    options.novomesto     : "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_NOVO-MES_history.html",
    options.maribor       : "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_MARIBOR_SLIVNICA_history.html",
    options.murska_sobota : "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_MURSK-SOB_history.html",
    options.nova_gorica   : "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_NOVA-GOR_history.html",
    options.portoroz      : "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_PORTOROZ_SECOVLJE_history.html",
}

meteo_url = ""
# Select the correct url
for city in cities:
    if (city):
        meteo_url = urls[city]
        break

# Try to get the website
try:
    uclient = ureq(meteo_url)
except urlerr.URLError:
    sys.exit(-1)

# Read and parse the website
raw = uclient.read()
uclient.close()

page_soup = soup(raw, "html.parser")

# Output the requested info
# If nothing is request output everything
if (options.temp_only):
    temp = page_soup.findAll("td", {"class":"t"})[0].text

    # Write the output in the desired unit(default -˚C)
    if (options.kelvin):
        print(f"{int(temp)+273}K")
    else:
        print(f"{temp}˚C")
elif (options.time):
    time = page_soup.findAll("td", {"class":"meteoSI-th"})[0].text

    print(f"{time}")
elif (options.weather):
    weather = page_soup.findAll("td", {"class":"wwsyn_longText"})[0].text

    print(f"{weather}")
else:
    temp = page_soup.findAll("td", {"class":"t"})[0].text
    weather = page_soup.findAll("td", {"class":"wwsyn_longText"})[0].text
    time = page_soup.findAll("td", {"class":"meteoSI-th"})[0].text

    print(f"{time}: {weather} ", end='')
    # Write the output in the desired unit(default -˚C)
    if (options.kelvin):
        print(f"{int(temp)+273}K")
    else:
        print(f"{temp}˚C")
