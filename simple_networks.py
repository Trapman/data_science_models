#(1) Finding Key Connectors:
#list of users, each represented by a dict that contains a user id and a user name:

users = [
  {"id": 0, "name": "Trap"},
  {"id": 1, "name": "Mega"},
  {"id": 2, "name": "David"},
  {"id": 3, "name": "Bradley"},
  {"id": 4, "name": "Scarbro"},
  {"id": 5, "name": "Comas"},
  {"id": 6, "name": "Dom"},
  {"id": 7, "name": "Noke"},
  {"id": 8, "name": "Chris"},
  {"id": 9, "name": "Trey"}
]

#list of "friendship" data, represented by a list of pairs of IDs:

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),  
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
               
#for example, the tuple (0, 1) indicates that the user with id 0 (Trap) and the user with id 1 (Mega) are friends.

#we could add a list of friends to each user like this:

for user in users:
  user["friends"] = []
  
#and then populate the lists using the friendship data:

for i, j in friendships:
  #this works because users[i] is the user whose id is i
  users[i]["friends"].append(users[j])     #this adds i as a friend of j
  users[j]["friends"].append(users[i])     #this adds j as a friend of i
  
#once each user dict contains a list of friends, we can easily do other calculations, such as the average number of connections:
#first we find the total number of connections, which we do by summing up the lengths of all of friends lists:

  def number_of_friends(user):
    """how many friends does user have?"""
    return len(user["friends"])       #length of friend_ids list
    
  total_connections = sum(number_of_friends(user) for user in users)
  
#then we just divide by the number of users:
  from __future__ import division      #to do long division
  num_users = len(users)               #length of the users list
  avg_connections = total_connections / num_users
  
#finding the most connected people (i.e. the people with the most friends):

#sort users from most friends to least friends:
  #create a list (user_id, number_of_friends)
  num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
  
  sorted(num_friends_by_id,                                 #gets it sorted
         key=lambda (user_id, num_friends): num_friends,    #by num_friends
         reverse = True)                                    #largest to smallest
         
  #each pair is (user_id, num_friends)
  #[(1,3), (), (), (), (), 
    (), (), (), (), ()]

#finding friends of friend: for each of a user's friends, iterate over that person's friends and collect all the results
  
  def friends_of_friend_ids_bad(user):
    #"foaf" abbreviation for "friend of a friend"
    return [foaf["id"]
      for friend in user["friends"]     #for each of user's friends
      for foaf in friend["friends]]     #get each of _their_ friends
      
#create a count of mutual friends between users, as well as a helper function to exlcude people already known to the user:

  from collections import Counter
  
  def not_the_same(user, other_user):
  """two uers are not the same if they have different ids"""
  return user["id"] != other_user["id"]
  
  def not_friends(user, other_user):
  """other_user is not a friend if he's not in user["friends"]
  return all(not_the_same(friend, other_user) for friend in user["friends"])
  
  def friends_of_friend_id(user):
    return Counter(foaf["id"]
      for friend in user["friends"] #for each of my friends
      for foaf in friend["friends"] #count *their* friends
      if not_the_same(user, foaf)   #who aren't me
      and not_friends(user, foaf))  #and aren't my friends
      
  print(friends_of_friend_ids(users[3])    
  
#(2) Salaries and Experience:

#finish building out examples...
