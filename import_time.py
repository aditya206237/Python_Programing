import time

def greet():
    hour = time.localtime().tm_hour
    
    if hour < 12:
        return "Good morning!"
    else:
        if hour < 18:
            return "Good afternoon!"
        else:
            if hour < 22:
                return "Good evening!"
            else:
                return "Hello!"
print("Current time is:-",time.asctime())
print(greet())