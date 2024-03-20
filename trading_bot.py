
import datetime
import requests

def time_converter_from_millis(ms_time):
    dt = datetime.datetime.fromtimestamp(ms_time // 1000.0)
    print(dt) #format 2024-03-13 00:10:00+00:00

#convert_time = 1710288600000
#time_converter_from_millis(convert_time)

def time_converter_to_millis(time_utc):
    dt_obj = datetime.datetime.strptime(time_utc, '%Y-%m-%d %H:%M:%S')
    millisec = int(dt_obj.timestamp() * 1000)
    return(millisec)

my_time = '2024-03-17 11:15:00'
time_converter_to_millis(my_time)

def time_adder(start_time, time_diff_min):
    new_time = start_time + datetime.timedelta(minutes=time_diff_min)
    return(new_time) #returns datetime obj

#my_time = datetime.datetime.now()
#print(time_adder(my_time, 5))

def decision_maker(my_list):
    start_price = my_list[0]
    if start_price - min(my_list) >= 1500:
        print("Sell, stop-loss")
    elif max(my_list) - start_price >= 700:
        print("Buy, take-profit")
        #print(max(my_list), start_price)
    elif start_price - min(my_list) >= 500:
        print("Buy")
    else:
        print("Hold")

#test_list = [65473.6, 65517.1, 65413.8, 65429.32, 65429.33, 65533.92, 65290.0, 65345.59, 65345.6, 65612.0, 65327.5, 65545.48, 65545.49, 65814.74, 65545.48, 65789.52, 65789.53, 66059.0, 65711.78, 66047.73, 66047.72, 66320.0, 65984.23, 66296.12, 66296.12, 66324.05, 66121.1, 66316.71]
#decision_maker(test_list)

def trading_bot(my_url, start_time, period_min): #seems to work!
    start_time_ms = time_converter_to_millis(start_time)
    start_time_dt = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time = time_adder(start_time_dt, period_min)
    end_time_ms = time_converter_to_millis(str(end_time))
    new_url = my_url + "&startTime=" + str(start_time_ms) + "&endTime=" + str(end_time_ms)
    #print(new_url)
    response = requests.get(new_url).json()
    prices = []
    for i in range(len(response)):
        response[i] = response[i][:5]
        #print(response[i])
        for k in range(1, 5):
            new_price = float(response[i][k])
            prices.append(new_price)
    #print(prices)
    decision_maker(prices)

test_url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m"
test_start_time = '2024-03-17 11:10:00' #1710663000000
test_period_min = 30
trading_bot(test_url, test_start_time, test_period_min)

#my_url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m"
#start_time = '2024-03-17 11:10:00' #1710663000000
#start_time_ms = time_converter_to_millis(start_time)
#start_time_dt = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
#end_time = time_adder(start_time_dt, 30)
#end_time_ms = time_converter_to_millis(str(end_time))
#new_url = my_url + "&startTime=" + str(start_time_ms) + "&endTime=" + str(end_time_ms)
#print(new_url)
#response = requests.get(new_url).json()
#prices = []
#for i in range(len(response)):
    #response[i] = response[i][:5]
    #print(response[i])
    #for k in range(1, 5):
        #new_price = float(response[i][k])
        #prices.append(new_price)
#print(prices)
#decision_maker(prices)













#my_url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=5m"
#start_time = '2024-03-17 11:10:00' #1710663000000
#start_time_ms = time_converter_to_millis(start_time)
#end_time = '2024-03-17 11:15:00'   #1710663300000
#end_time_ms = time_converter_to_millis(end_time)
#print(start_time_ms, end_time_ms)
#new_url = my_url + "&startTime=" + str(start_time_ms) + "&endTime=" + str(end_time_ms)
#print(new_url)
#response = requests.get(new_url).json()
#for i in range(len(response)):
    #response[i] = response[i][:5]
    #print(response[i])








#def price_checker(my_list):
    #actions = []
    #for i in range(len(my_list)):
        #if my_list[0] - my_list[i] >= 1500:
            #actions.append("sell")
        #elif my_list[0] - my_list[i] > 500:
            #actions.append("buy")
        #elif my_list[i] - my_list[0] >= 700:
            #actions.append("sell")
        #else:
            #actions.append("hold")
    #print(actions)


#test_list = [1201, 1205, 1311, 1195, 700, 1428]
#price_checker(test_list)
                                  
        
