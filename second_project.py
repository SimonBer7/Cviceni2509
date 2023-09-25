
map = {
    "Vltava": ["Sumava", "Praha", "Ceske Budejovice", "Slapy"],
    "Labe": ["Krkonose", "Podebrady", "Melnik", "Nymburk"],
    "Berounka": ["Plzen", "Beroun", "Krivoklat", "Roztoky"]
}
""""
map2 = {
    ["Praha", "Ceske Budejovice", "Slapy"]: "Vltava",
    ["Podebrady", "Melnik", "Nymburk"]: "Labe",
    ["Beroun", "Krivoklat", "Roztoky"]: "Berounka"
}
"""

def getRiver():
    river = input("Zadej reku: ")

    if river in map.keys():
        print("Reka "+str(river)+" prameni v "+map[river][0]+", mesta: "+map[river][1]+", "+map[river][2]+", "+map[river][3])
    else:
        raise ValueError

def getTowns():
    town = input("Zadej mesto: ")

    for x in map2.keys():
        if town in map2.keys()[x]:
            print("Mestem "+str(town)+" proteka reka "+map2[town])
        else:
            raise ValueError




choice = input("1) R => M\n2) M => R\nVase volba: ")
if choice == "1":
    getRiver()
elif choice == "2":
    getTowns()
else:
    print("Error, vyberte 1/2")
