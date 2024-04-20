count = 0

# while condition :
    # code to execute while the condition is true

# while count < 5 :
#     print("Sailing the python seas" , count)
#     count += 1

# # example
# for island in ["Tortugo" , "Skull Island" , "Davy Jone's Island"] :
#     print("Now visiting" , island)


# flashes = 0

# while flashes < 5 :
#     print("Lighthouse flash")
#     flashes += 1


# # infinite loop

# while True :
#     print("adrift at  sea")



# for item in sequence :
    # code to execute for each item


# treasure_map = ["Cave" , "Waterfall" ,"Old Shipwreck"]

# for location in treasure_map : 
#     print("Searching for" , location)


# for day in range(1 , 8) :
#     print("Sending out the scout parrot on day" , day)

# supplies = ["Biscuits" , "Scurvy Medicine" , "rum"]

# for day in range(1,8) :
#     print("Day" , day , "log : ")
#     for supply in supplies : 
#         print("-Used" , supply)


# for number in range(1,11) : 
#     if number % 2 == 0:
#         print(number , "is even")
#     else :
#         print(number, "is odd")


# fleet = {
#     "Sloop" : ["Tortugo" , "Barbados" ,"Jamaica"],
#     "Brigantine" : ["Bermuda" ,"St. Kitts"],
#     "Galleon" : ["Port Royal" , "Nassau" , "Havana"]
# }

# for ship , ports  in fleet.items() : 
#     print("The " , ship , "will visit") 
#     for port in ports : 
#         print("-", port)
#     # print("The ship name is " , ship)


# cargo_lists = {
#     "Sloop" : ["Spices" , "Silk" , "Golden Goblet"],
#     "Brigantine" : ["Rum" , "Timber"],
#     "Galleon" : ["Sugar" , "Golden Goblet" , "Coffee"]
# }


# for ship , cargo in cargo_lists.items():
#     print("Inspecting cargo of the " ,ship)
#     if 'Golden Goblet' in cargo :
#         print("Precious item found ")
#     else :
#         print("No precious item found ")




# treasure_chest = ["Gold Coin", "Silver Coin", "Jewels" , "Pearl"]


# for item in treasure_chest :
#     print(item , " ")
#     if item == 'Silver Coin' :
#         print("We found silver coin")
#         break


# break keyword breaks out of the loop 
# continue skips the current iteration
# continue prevents the execution of the rest of the loops body



for number in range(1,10) : 
    if number % 2 == 0:
        continue
    print(number , "is odd") 