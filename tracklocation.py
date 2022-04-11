import phonenumbers
from phonenumbers import geocoder

number = input("Masukkan No telepon: ")
ch_number = phonenumbers.parse(number, 'CH')

print(geocoder.description_for_number(ch_number, "id"))

from phonenumbers import carrier

s_num = phonenumbers.parse(number, 'RO')
print(carrier.name_for_number(s_num, "id"))