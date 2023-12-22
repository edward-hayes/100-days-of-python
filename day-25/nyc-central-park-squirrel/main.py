import pandas

INPUT_PATH = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
OUPUT_PATH = "squirrel_count.csv"

data = pandas.read_csv(INPUT_PATH)

#----------------solution 1 ---------------------#
#result_data = data.groupby(['Primary Fur Color'])['Primary Fur Color'].count()
#result_data.to_csv(OUPUT_PATH)

# -----------------solution 2 -------------------#

#fur_color = data['Primary Fur Color'].dropna().unique().tolist()

# count_of_color = []

# for color in fur_color:
#     squirrel_color_table = data[data['Primary Fur Color'] == color]
#     count = squirrel_color_table['Primary Fur Color'].count()
#     count_of_color.append(count)

# result_data = pandas.DataFrame(list(zip(fur_color, count_of_color)),columns=['Primary Fur Color','Count'])

# result_data.to_csv(OUPUT_PATH)

# --------------------solution 3 ------------------#

fur_color = data['Primary Fur Color'].dropna().unique().tolist()

count_of_color = []

for color in fur_color:
    squirrel_color_table = data[data['Primary Fur Color'] == color]
    count = squirrel_color_table['Primary Fur Color'].count()
    count_of_color.append(count)

data_dict = {
    "Primary Fur Color" : fur_color,
    "Count" : count_of_color
}

result_data = pandas.DataFrame(data_dict)

result_data.to_csv(OUPUT_PATH)