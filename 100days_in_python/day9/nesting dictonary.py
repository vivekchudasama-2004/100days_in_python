capitals={
    "france": "paris",
    "germany": "berlin"
}
#nesting list in dictonary

travel_log={
    "france": ["paris","lille","dijon"]
}

capitals.update(travel_log)
print(capitals)

#nesting dictonary in dictonary
travel_log={
    "france":{"cities_visited":["paris","lille","dijon"], "total_visits":12}
}
print(travel_log)

#nesting dictonary inside list

city=[
    {
     "country":"france",
     "cities_visited" : ["paris", "lille", "dijon"],
     "total_visits" : 12

    },
    {
        "france":"lille",
        "germany":"berlin"
}]
print(city[0])
