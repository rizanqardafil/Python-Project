from covid import Covid
covid = Covid()
cases = covid.get_status_by_country_name("china")
for x in cases:
    print(x,":",cases[x])
