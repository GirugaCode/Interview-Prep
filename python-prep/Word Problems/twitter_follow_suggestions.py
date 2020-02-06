"""
New Problem: Twitter Follow Suggestions
You’re working an internship at Twitter and are tasked to improve suggestions 
for accounts to follow, which already works great for established accounts because 
it uses content from your tweets and other accounts you follow to suggest new ones. 
However, when a new user signs up none of this information exists yet, but Twitter 
still wants to make some follow suggestions. Your team asked you to implement a function 
that accepts a new user’s handle and an array of many other users’ handles, which could be 
very long – Twitter has over 330 million active accounts! You need to calculate a similarity score 
between a pair of handles by looking at the letters each contains, scoring +1 for each letter in 
the alphabet that occurs in both handles but scoring –1 for each letter that occurs in only one handle. 
Your function should return k handles from the array that have the highest similarity score to the new user’s handle.

Restatment of the problem:
Given a new user handle go over a list of exisiting user handles using a 
similarty point system to find two users with the most similarity based on the handles name.

Example execution:
handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
suggest('iLoveDogs', handles, k=2)   should return   ['GodIsLove', 'DogeCoin']

Possible Simplifications

Find only 1 handle with the highest similarity, then later try to find 2, and then k handles.
Implement only a similarity score helper function, then later use it to find similar handles.
When calculating similarity scores, only count +1 for matching letters at first, then later include –1 for non-matching letters.
Make letter matching case sensitive at first, then later make matching case insensitive.

"""
def suggest(new_user, list_of_users, k):
    # Put the list_of_users in a dictionary where the
        # Key -> Username
        # Value -> counter for similarity
    # Create a counter for similarity 
    # Iterate through the dictionary 
        # Compare each letter in every Key to every letter in the new_user
            # If the letter is found
                # Increase that keys value 
    # Return that key with that largest value
    user_dict = dict.fromkeys(list_of_users, 0)
    print(new_user)
    for key, value in user_dict.items():
        print("key:", key)
        print("value:", value)
        for character in key:
            print("character:", character)
            if character in new_user:
                user_dict[key] += 1
            else:
                user_dict[key] -= 1
                
    return sorted(user_dict.items(), key=lambda x: x[1], reverse=True)[:k]

print(suggest('iLoveDogs', ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust'], 2))



