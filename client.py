import os, tools
class Client():
    def __init__(self):
        self.username = ""
        self.password = "" # stored in hash
    def login(self, username, password):
        if self.load(username) == True:
            if self.password == tools.sha256(password):
                return True
            else:
                return False
        else:
            return False
    def isInUse(self, username):
        usernames = os.listdir("users/")
        f = username
        for username in usernames:
            if f == username:
                return True
        return False
    def load(self, username):
        self.username = username
        if self.username != "":
            filename = "users/" + self.username
            if os.path.isfile(filename) == True:
                with open(filename, "r") as f:
                    self.password = f.read()
                    return True
            else:
                return False
        else:
            return False
        return False
    def register(self, username, password, dont_hash):
        self.username = username
        self.password = password
        if self.username != "" and self.password != "":
            filename = "users/" + self.username
            if os.path.isfile(filename) == False:
                with open(filename, "w") as f:
                    if dont_hash == True:
                        f.write(self.password)
                        return True
                    else:
                        f.write(tools.sha256(self.password))
                        return True
            else:
                return False
        else:
            return False
    def remove(self):
        if self.username != "" and self.password != "":
            filename = "users/" + self.username
            if os.path.isfile(filename) == True:
                os.remove(filename)
                return True
            else:
                return False
        else:
            return False
    def change(self, modifier, new):
        if modifier == "username":
            self.remove()
            self.username = new
            self.register(self.username, self.password, True)
            return True
        elif modifier == "password":
            filename = "users/" + self.username
            with open(filename, "w") as f:
                f.write(tools.sha256(new))
            self.password = new
            return True
        return False
