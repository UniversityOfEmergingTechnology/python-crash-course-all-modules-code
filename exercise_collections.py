# user_data : dictionary and tuple
# posts : list
# tags : set


users = {
    "user1" : ("user1@example.com" , 25),
    "user2" : ("user2@example.com" , 30)
}

# posts

posts = [
    "Python is awesome" ,
    "Tuples and lists are super useful"
]

# tags

tags = {"Python" , "Coding" , "tutorial"}

# integrating

forum_database = {
    "users" : users ,
    "posts" : posts ,
    "tags" : tags
}

# example operation adding a new post

new_post = "Exploring python collections is fun"

posts.append(new_post)

# adding a new tag
tags.update({"Collections" , "Learning"})

print(forum_database)