import phonenumbers

from test0 import number

from phonenumbers import geocoder, carrier

country = phonenumbers.parse(number, "CH")

print(geocoder.description_for_number(country, "en"))

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
