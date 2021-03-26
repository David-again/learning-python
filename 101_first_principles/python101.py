# def greeting(name, department):
#     print("Welcome, " + name)
#     print("Your name is: ", name)
    
    
def calc_seconds(hours, minutes, seconds):
    min_sec = minutes*60
    hour_sec = hours*3600
    newsec = seconds
    return hour_sec + min_sec + newsec

print(calc_seconds(1,3,2))
