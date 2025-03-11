import json
import os

class Database:

  def insert(self,name,email,password):
    
    if os.path.exists('users.json'):
      with open('users.json', 'r') as rf:
        try:
          users = json.load(rf)
        except json.JSONDecodeError:
          users = {}  


        if email in users: 
         return 0
        else:
          users[email] = [name,password]


      with open('users.json', 'w') as wf:
        json.dump(users,wf)
        return 1