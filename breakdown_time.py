def breakdown_time(seconds):
    if seconds < 0 or type(seconds)!= int:
        return -1
    elif seconds == 0:
        return {}
    else:
        a=seconds//3600
        b=(seconds%3600)//60
        c=((seconds%3600)%60)
        dictionary = { a :"h", b : "m", c : "s"}
        return dictionary