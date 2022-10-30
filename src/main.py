from urllib.request import urlopen as ureq
from urllib import error as urlerr
from bs4 import BeautifulSoup as soup
import re
import time as t
import sys
from opts import getOpts

options = getOpts(sys.argv[1:])
meteo_url = ""
# Select the correct url
if (options.ljubljana):
    meteo_url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_LJUBL-ANA_BEZIGRAD_history.html"
elif (options.novomesto):
    meteo_url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_NOVO-MES_history.html" 

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
if (options.celsius):
    temps = page_soup.findAll("td", {"class":"t"})

    temp = temps[0].text
    print(f"{temp}°C")
elif (options.time):
    times = page_soup.findAll("td", {"class":"meteoSI-th"})

    time = times[0].text
    print(f"{time}")
else:
    temps = page_soup.findAll("td", {"class":"t"})
    weathers = page_soup.findAll("td", {"class":"wwsyn_longText"})
    times = page_soup.findAll("td", {"class":"meteoSI-th"})

    temp = temps[0].text
    weather = weathers[0].text
    time = times[0].text

    print(f"{time}: {weather} {temp}°C")
