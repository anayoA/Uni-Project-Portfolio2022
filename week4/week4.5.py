def fahconv(x):
    celc = ((x-32) * 5) // 9
    return celc

def celcconv(x):
    fah = ((x * 9) // 5) + 32
    return fah

print(celcconv(22))
print(fahconv(88))