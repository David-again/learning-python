def convert_to_celsius(x):
    return (x-32)*5/9

for tempFahrenheit in range(0,101,10):
    # txt1 = ("{tempFahrenheit}, {tempCelsius}".format(tempFahrenheit=tempFahrenheit, tempCelsius = convert_to_celsius(tempFahrenheit)))
    # print(txt1)

    print(("{tempFahrenheit:>3} F ||  {tempCelsius:6.2f} C".format(tempFahrenheit=tempFahrenheit, tempCelsius = convert_to_celsius(tempFahrenheit))))
    