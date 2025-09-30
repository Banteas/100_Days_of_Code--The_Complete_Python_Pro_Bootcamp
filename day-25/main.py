
import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# 1st solution
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

summary_df = pandas.DataFrame(data_dict)
summary_df.to_csv("squirrel_summary.csv")

# 2nd solution
colors = ("Gray", "Cinnamon", "Black")
my_squirrel_dict = {}
for color in colors:
    squirrels = data[data["Primary Fur Color"] == color]
    my_squirrel_dict[color] = len(squirrels)




squi_data = pandas.DataFrame({
    "Fur Color": list(my_squirrel_dict.keys()),
    "Count": list(my_squirrel_dict.values())
})

squi_data.to_csv("squirrel_count.csv")

