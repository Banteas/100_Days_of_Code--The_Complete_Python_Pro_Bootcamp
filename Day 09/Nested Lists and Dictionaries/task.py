# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
# # print Lille
# print(travel_log["France"][1])
# #print Berlin
# germany_towns = travel_log["Germany"]
# second_ger_town = germany_towns[1]
# print(second_ger_town)
#
# #print "D"
# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
    "cities_visited":["Berlin","Hamburg", "Stuttgart"],
    "total_visits": 5
    },
}
# print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])
