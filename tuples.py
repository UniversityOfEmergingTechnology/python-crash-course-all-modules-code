location = (13.4125 , 103.86667)

print(f'The coordinates for Angkor Wat are Latitude {location[0]} , Longitude {location[1]}')


# tuples in data storage

users = [("Alice" , (1992 , 5, 16)) , ("Bob" , (1985 , 8 , 23))]


print(f"{users[0][0]}'s birth year is {users[0][1][0]}")


# modify a list

users[0] = ("Alicia" , users[0][1])

print(f"{users[0][0]}'s birth year is {users[0][1][0]}")

