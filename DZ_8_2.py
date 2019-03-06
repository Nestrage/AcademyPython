import string

country_dict = {}
def make_country(country: string, capital: string):
    country_dict[country] = capital
    return

make_country("Norway", "Oslo")
make_country("Ukraine","Kyiv")
make_country("Deuthcland", "Berlin")
print(country_dict)