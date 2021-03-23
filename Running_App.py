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


    print('                         +++++ TABLE OF SCORES +++++')
    width = 76
    print("-" * width)
    print("| Distance(km) |     Time     |    Pace/km   |   Calories   |     Date     |")
    print("*" * width)
    for idx in range(0, len(table_of_date)):
        print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format(str(table_of_distance[idx]), table_of_time[idx], table_of_pace[idx] , str(table_of_calories[idx]), str(table_of_date[idx])))
        # print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format('two', "", "", '', ''))
        # print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format('three', "", "", '', ''))
        # print("|  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |  {:10s}  |" .format('four', "", "", '', ''))
        print("-" * width)

        
