# def greet_visitor(name):
#     print("Welcome aboard " , name)

# name = "Mudit"
# greet_visitor(name)


# def plot_course(destination , distance) :
#     print("Plotting the course")
#     print("Destination : ", destination)
#     print("Distance : ", distance)


# plot_course("Skull Island" , "20 nautical miles")


# def calculate_provision(crew_size , journey_length):
#     print("Journey Length : ", journey_length)
#     return crew_size * journey_length * 2

# result = calculate_provision( 10 , 5 )

# print("We need to pack " , result , " units of provisions")



def count_treasure_coins(coins , bars) :
    total_gold = coins * 10 + bars * 20
    return total_gold

treasure_coins = count_treasure_coins(50 , 30)
print(treasure_coins)