import datetime

date_and_time = datetime.datetime.now()

table_of_distance = []
table_of_time = []
table_of_pace = []
table_of_calories = []
table_of_date = []

print('###')
print('     Actual datetime is: ' + date_and_time.strftime('%H:%M %p | %d-%m-%Y'))
print('             Good morning PRZEMO :)\n    Please enter Your today score of running: ')
print('###')

while True:
    date = date_and_time.strftime('%d-%m-%Y')
    table_of_date.append(date)

    distance = float(input('Enter distance (km): '))
    table_of_distance.append(distance)
    time1 = int(input('Enter time (h): '))
    time2 = int(input('Enter time (min): '))
    time3 = int(input('Enter time (sec): '))

    # running_pace()
    # def running_pace():
    hours_sec = time1 * 3600
    minutes_sec = time2 * 60
    sec = time3
    average_running_pace_in_sec = int((hours_sec + minutes_sec + sec) / distance)

    minutes, average_running_pace_in_sec = divmod(average_running_pace_in_sec, 60)
    hours, minutes = divmod(minutes, 60)
    average_running_pace = str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(average_running_pace_in_sec).zfill(2)
    table_of_pace.append(average_running_pace)
    print('Your average running pace is: ' + average_running_pace + ' (per km)')

    total_time = str(time1).zfill(2) + ':' + str(time2).zfill(2) + ':' + str(time3).zfill(2)
    table_of_time.append(total_time)
    calories = distance * 72
    table_of_calories.append(calories)
    print('You burned: ' + str(int(calories)) + ' calories.')
    if calories < 500:
        print('Not too bad, but You didnt burn even chocolate bar ;)' )
    elif calories >= 500 and calories < 1000:
        print('Good job, today You did your best :)' )
    else:
        print('Amazing!!! Please dont stop running like today, keep going :D')

    print()
    # print(total_time)
    # print(date)
    # print(table_of_distance)
    # print(table_of_time)
    # print(table_of_pace)
    # print(table_of_calories)
    # print(table_of_date)
    # x = len(table_of_distance)
    # print(x)

    while True:
        print('                         +++++ TABLE OF SCORES +++++')
        width = 76
        print("-" * width)
        print("| Distance(km) |     Time     |    Pace/km   |   Calories   |     Date     |")
        print("*" * width)
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[0]), table_of_time[0], table_of_pace[0] , str(table_of_calories[0]), str(table_of_date[0])))
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[1]), table_of_time[1], table_of_pace[1] , str(table_of_calories[1]), str(table_of_date[1])))
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[2]), table_of_time[2], table_of_pace[2] , str(table_of_calories[2]), str(table_of_date[2])))
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[3]), table_of_time[3], table_of_pace[3] , str(table_of_calories[3]), str(table_of_date[3])))
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[4]), table_of_time[4], table_of_pace[4] , str(table_of_calories[4]), str(table_of_date[4])))
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[5]), table_of_time[5], table_of_pace[5] , str(table_of_calories[5]), str(table_of_date[5])))
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[6]), table_of_time[6], table_of_pace[6] , str(table_of_calories[6]), str(table_of_date[6])))
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[7]), table_of_time[7], table_of_pace[7] , str(table_of_calories[7]), str(table_of_date[7])))
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[8]), table_of_time[8], table_of_pace[8] , str(table_of_calories[8]), str(table_of_date[8])))
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[9]), table_of_time[9], table_of_pace[9] , str(table_of_calories[9]), str(table_of_date[9])))
        # print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format('two', "", "", '', ''))
        # print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format('three', "", "", '', ''))
        # print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format('four', "", "", '', ''))
        print("-" * width)

        
