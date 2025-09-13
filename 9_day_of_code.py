# #nested lists nested dictionaroes

# programing_dictionary={
#     "Bug":"An error happens",
#     "function":"a piece of code that we can use it for multiple times.",
#     "loop":"the action of doing something over and over again."
#     }

# print(programing_dictionary["Bug"])
# programing_dictionary["loop"]="something for you"
# print(programing_dictionary["loop"])

# empty_dictionary={}

# #write an existing dictionary
# programing_dictionary={}
# print(programing_dictionary)


# programing_dictionary["Bug"]="A math in your computer."
# print(programing_dictionary)

# #loop through dictionary

# for key in programing_dictionary:
#     print(key)

#nesting dectionary and list

capitals={
    "france":"paris",
    "germany":"Barlin",
}

# travel_log={
#     "france":["Paris","lille","Dijon"],
#     "germany":["stuttgart","berlin"],
# }



# print(travel_log["france"])
# print(travel_log["france"][1])
# nested_list=["A","b",["c","d"]]
# print(nested_list[2][0])
travel_log={
    "france":{
        "num_times_visited":8,
        "cities_visited":["paris","lille","dijon"]
    },
    "germany":{
      "cities_visited":["stuttgart","berlin"],
      "total_visits":5
    }
}


print(travel_log["france"]["num_times_visited"])
print(travel_log["france"]["cities_visited"][0])
