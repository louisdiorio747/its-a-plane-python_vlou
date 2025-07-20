ZONE_HOME = {
    "tl_y": xx.672948, # Top-Left Latitude (deg) https://www.latlong.net/ or google maps. The bigger the zone, the more planes you'll get. My zone is ~3.5 miles in each direction or 10mi corner to corner. 
    "tl_x": -xx.xxxxxx, # Top-Left Longitude (deg)
    "br_y": xx.798340, # Bottom-Right Latitude (deg)
    "br_x": -xx.014551 # Bottom-Right Longitude (deg)
}
LOCATION_HOME = [
    xx.xxxxxx, # Latitude (deg)
    -xx.xxxxxx, # Longitude (deg)
    x.xx #alt
]
WEATHER_LOCATION = "washington" #same as location home
TOMORROW_API_KEY = "A5y32PYQlIe3nMoCuKsgQLXXroteResJ" # Get an API key from https://tomorrow.io they only allows 25 pulls an hour, if you reach the limit you'll need to wait until the next hour 
TEMPERATURE_UNITS = "imperial" #can use "metric" if you want, same for distance 
DISTANCE_UNITS = "imperial"
# CLOCK_FORMAT = "12hr" #use 12hr or 24hr
MIN_ALTITUDE = 0 #feet above sea level. If you live at 1000ft then you'd want to make yours ~3600 etc. I use 2600 to weed out some of the smaller general aviation traffic. 
BRIGHTNESS = 90
BRIGHTNESS_NIGHT = 30
NIGHT_BRIGHTNESS = False #True for on False for off
NIGHT_START = "22:00" #dims screen between these hours
NIGHT_END = "06:00"
GPIO_SLOWDOWN = 2 #depends what Pi you have I use 2 for Pi 3 and 1 for Pi Zero
JOURNEY_CODE_SELECTED = "" #your home airport code
JOURNEY_BLANK_FILLER = " N/A " #what to display if theres no airport code
HAT_PWM_ENABLED = False #only if you haven't soldered the PWM bridge use True if you did
FORECAST_DAYS = 1 #today plus the next two days
