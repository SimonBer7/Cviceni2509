map = {
    "Plzen": "Plzensky kraj",
    "Ceske Budejovice": "Jihocesky kraj",
    "Kladno": "Stredocesky kraj",
    "Liberec": "Liberecky kraj",
    "Pardubice": "Pardubicky kraj"
}

map2 = {
    "Plzensky kraj": "Plzen",
    "Jihocesky kraj": "Ceske Budejovice",
    "Stredocesky kraj": "Kladno",
    "Liberecky kraj": "Liberec",
    "Pardubicky kraj": "Pardubice"
}

def getTown():
    town = input("Zadej mesto: ")
    if town in map.keys():
        print(map[town])
    else:
        raise ValueError



def getCountry():
    country = input("Zadej kraj: ")
    if country in map2.keys():
        print(map2[country])
    else:
        raise ValueError



choice = input("1) M => K\n2) K => M\nVase volba: ")
if choice == "1":
    getTown()
elif choice == "2":
    getCountry()
else:
    print("Error, vyberte 1/2")


