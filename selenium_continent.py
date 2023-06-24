# import selenium.webdriver as wd
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import openpyxl as xl
# import os
#
# driver_path="C:/Users/Admin/Desktop/pythonpractice/chromedriver.exe"
# driver=wd.Chrome(driver_path)
# driver.get("https://www.geonames.org/countries/")
# wait=WebDriverWait(driver,10)
# target_tr=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"table#countries tbody tr")))
# dict={}
# for i in target_tr:
#     target_td=i.find_elements(By.TAG_NAME,"td")
#     if len(target_td)>=9:
#         target_country_a=target_td[4].find_element(By.TAG_NAME,"a")
#         target_continent=target_td[8].text
#         dict[target_country_a.text]=target_continent
# print(dict)

# dict_countries_continents = {'Andorra': 'EU', 'United Arab Emirates': 'AS', 'Afghanistan': 'AS',
#                              'Antigua and Barbuda': 'NA', 'Anguilla': 'NA', 'Albania': 'EU', 'Armenia': 'AS',
#                              'Angola': 'AF', 'Antarctica': 'AN', 'Argentina': 'SA', 'American Samoa': 'OC',
#                              'Austria': 'EU', 'Australia': 'OC', 'Aruba': 'NA', 'Åland': 'EU', 'Azerbaijan': 'AS',
#                              'Bosnia and Herzegovina': 'EU', 'Barbados': 'NA', 'Bangladesh': 'AS', 'Belgium': 'EU',
#                              'Burkina Faso': 'AF', 'Bulgaria': 'EU', 'Bahrain': 'AS', 'Burundi': 'AF', 'Benin': 'AF',
#                              'Saint Barthélemy': 'NA', 'Bermuda': 'NA', 'Brunei': 'AS', 'Bolivia': 'SA',
#                              'Bonaire, Sint Eustatius, and Saba': 'NA', 'Brazil': 'SA', 'Bahamas': 'NA', 'Bhutan': 'AS',
#                              'Bouvet Island': 'AN', 'Botswana': 'AF', 'Belarus': 'EU', 'Belize': 'NA', 'Canada': 'NA',
#                              'Cocos (Keeling) Islands': 'AS', 'DR Congo': 'AF', 'Central African Republic': 'AF',
#                              'Congo Republic': 'AF', 'Switzerland': 'EU', 'Ivory Coast': 'AF', 'Cook Islands': 'OC',
#                              'Chile': 'SA', 'Cameroon': 'AF', 'China': 'AS', 'Colombia': 'SA', 'Costa Rica': 'NA',
#                              'Cuba': 'NA', 'Cabo Verde': 'AF', 'Curaçao': 'NA', 'Christmas Island': 'OC',
#                              'Cyprus': 'EU', 'Czechia': 'EU', 'Germany': 'EU', 'Djibouti': 'AF', 'Denmark': 'EU',
#                              'Dominica': 'NA', 'Dominican Republic': 'NA', 'Algeria': 'AF', 'Ecuador': 'SA',
#                              'Estonia': 'EU', 'Egypt': 'AF', 'Western Sahara': 'AF', 'Eritrea': 'AF', 'Spain': 'EU',
#                              'Ethiopia': 'AF', 'Finland': 'EU', 'Fiji': 'OC', 'Falkland Islands': 'SA',
#                              'Micronesia': 'OC', 'Faroe Islands': 'EU', 'France': 'EU', 'Gabon': 'AF',
#                              'United Kingdom': 'EU', 'Grenada': 'NA', 'Georgia': 'AS', 'French Guiana': 'SA',
#                              'Guernsey': 'EU', 'Ghana': 'AF', 'Gibraltar': 'EU', 'Greenland': 'NA', 'The Gambia': 'AF',
#                              'Guinea': 'AF', 'Guadeloupe': 'NA', 'Equatorial Guinea': 'AF', 'Greece': 'EU',
#                              'South Georgia and South Sandwich Islands': 'AN', 'Guatemala': 'NA', 'Guam': 'OC',
#                              'Guinea-Bissau': 'AF', 'Guyana': 'SA', 'Hong Kong': 'AS',
#                              'Heard and McDonald Islands': 'AN', 'Honduras': 'NA', 'Croatia': 'EU', 'Haiti': 'NA',
#                              'Hungary': 'EU', 'Indonesia': 'AS', 'Ireland': 'EU', 'Israel': 'AS', 'Isle of Man': 'EU',
#                              'India': 'AS', 'British Indian Ocean Territory': 'AS', 'Iraq': 'AS', 'Iran': 'AS',
#                              'Iceland': 'EU', 'Italy': 'EU', 'Jersey': 'EU', 'Jamaica': 'NA', 'Jordan': 'AS',
#                              'Japan': 'AS', 'Kenya': 'AF', 'Kyrgyzstan': 'AS', 'Cambodia': 'AS', 'Kiribati': 'OC',
#                              'Comoros': 'AF', 'St Kitts and Nevis': 'NA', 'North Korea': 'AS', 'South Korea': 'AS',
#                              'Kuwait': 'AS', 'Cayman Islands': 'NA', 'Kazakhstan': 'AS', 'Laos': 'AS', 'Lebanon': 'AS',
#                              'Saint Lucia': 'NA', 'Liechtenstein': 'EU', 'Sri Lanka': 'AS', 'Liberia': 'AF',
#                              'Lesotho': 'AF', 'Lithuania': 'EU', 'Luxembourg': 'EU', 'Latvia': 'EU', 'Libya': 'AF',
#                              'Morocco': 'AF', 'Monaco': 'EU', 'Moldova': 'EU', 'Montenegro': 'EU', 'Saint Martin': 'NA',
#                              'Madagascar': 'AF', 'Marshall Islands': 'OC', 'North Macedonia': 'EU', 'Mali': 'AF',
#                              'Myanmar': 'AS', 'Mongolia': 'AS', 'Macao': 'AS', 'Northern Mariana Islands': 'OC',
#                              'Martinique': 'NA', 'Mauritania': 'AF', 'Montserrat': 'NA', 'Malta': 'EU',
#                              'Mauritius': 'AF', 'Maldives': 'AS', 'Malawi': 'AF', 'Mexico': 'NA', 'Malaysia': 'AS',
#                              'Mozambique': 'AF', 'Namibia': 'AF', 'New Caledonia': 'OC', 'Niger': 'AF',
#                              'Norfolk Island': 'OC', 'Nigeria': 'AF', 'Nicaragua': 'NA', 'Netherlands': 'EU',
#                              'Norway': 'EU', 'Nepal': 'AS', 'Nauru': 'OC', 'Niue': 'OC', 'New Zealand': 'OC',
#                              'Oman': 'AS', 'Panama': 'NA', 'Peru': 'SA', 'French Polynesia': 'OC',
#                              'Papua New Guinea': 'OC', 'Philippines': 'AS', 'Pakistan': 'AS', 'Poland': 'EU',
#                              'Saint Pierre and Miquelon': 'NA', 'Pitcairn Islands': 'OC', 'Puerto Rico': 'NA',
#                              'Palestine': 'AS', 'Portugal': 'EU', 'Palau': 'OC', 'Paraguay': 'SA', 'Qatar': 'AS',
#                              'Réunion': 'AF', 'Romania': 'EU', 'Serbia': 'EU', 'Russia': 'EU', 'Rwanda': 'AF',
#                              'Saudi Arabia': 'AS', 'Solomon Islands': 'OC', 'Seychelles': 'AF', 'Sudan': 'AF',
#                              'Sweden': 'EU', 'Singapore': 'AS', 'Saint Helena': 'AF', 'Slovenia': 'EU',
#                              'Svalbard and Jan Mayen': 'EU', 'Slovakia': 'EU', 'Sierra Leone': 'AF', 'San Marino': 'EU',
#                              'Senegal': 'AF', 'Somalia': 'AF', 'Suriname': 'SA', 'South Sudan': 'AF',
#                              'São Tomé and Príncipe': 'AF', 'El Salvador': 'NA', 'Sint Maarten': 'NA', 'Syria': 'AS',
#                              'Eswatini': 'AF', 'Turks and Caicos Islands': 'NA', 'Chad': 'AF',
#                              'French Southern Territories': 'AN', 'Togo': 'AF', 'Thailand': 'AS', 'Tajikistan': 'AS',
#                              'Tokelau': 'OC', 'Timor-Leste': 'OC', 'Turkmenistan': 'AS', 'Tunisia': 'AF', 'Tonga': 'OC',
#                              'Turkey': 'AS', 'Trinidad and Tobago': 'NA', 'Tuvalu': 'OC', 'Taiwan': 'AS',
#                              'Tanzania': 'AF', 'Ukraine': 'EU', 'Uganda': 'AF', 'U.S. Outlying Islands': 'OC',
#                              'United States': 'NA', 'Uruguay': 'SA', 'Uzbekistan': 'AS', 'Vatican City': 'EU',
#                              'St Vincent and Grenadines': 'NA', 'Venezuela': 'SA', 'British Virgin Islands': 'NA',
#                              'U.S. Virgin Islands': 'NA', 'Vietnam': 'AS', 'Vanuatu': 'OC', 'Wallis and Futuna': 'OC',
#                              'Samoa': 'OC', 'Kosovo': 'EU', 'Yemen': 'AS', 'Mayotte': 'AF', 'South Africa': 'AF',
#                              'Zambia': 'AF', 'Zimbabwe': 'AF'}
# if "Pakistan" in dict_countries_continents.keys():
#     print(dict_countries_continents["Pakistan"])

import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path="C:/Users/Admin/Desktop/pythonpractice/chromedriver.exe"
driver=wd.Chrome(executable_path=driver_path)
driver.get("https://www.geonames.org/countries/")
wait=WebDriverWait(driver,10)
target_tr=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"table#countries tbody tr")))
dict={}
for i in target_tr:
    target_td=i.find_elements(By.TAG_NAME,"td")
    target_country_a=target_td[4].find_element(By.TAG_NAME,"a")
    target_continent=target_td[8].text
    dict[target_country_a.text]=target_continent
print(dict)





