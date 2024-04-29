
def decision_maker(next_tick_prices, order): 
    #https://gist.github.com/RodionGork/11f86590c0661ba86c7395bf10cff580?permalink_comment_id=5038230
    latest_ticks.append(next_tick_prices)
    if len(latest_ticks) <= 10:
        return("Still collecting data")
    else:
        #print(latest_ticks)
        latest_ticks.pop(0) #remove the 1st(oldest) tick
        #print(latest_ticks)
        start_price = latest_ticks[0][0]
        end_price = latest_ticks[9][3]
        if order != None: #we have BTC
            print(max(next_tick_prices), start_price)
            if start_price - min(next_tick_prices) >= 1500:
                action = "sell" #stop-loss
            elif max(next_tick_prices) - start_price >= 700:
                action = "sell" #take-profit
            else:
                action = "hold"
        else:
            #print(start_price, end_price)
            if start_price - end_price >= 500:
                action = "buy"
            else:
                action = "hold"
        return(action)
            
tick_1 = [1000, 1500, 900, 950]
tick_2 = [950, 1100, 890, 1010]
tick_3 = [1010, 1400, 1000, 1150]
tick_4 = [1150, 1360, 1050, 1050]
tick_5 = [1050, 1450, 990, 1200]
tick_6 = [1200, 1360, 1220, 1300]
tick_7 = [1300, 1490, 1200, 1250]
tick_8 = [1250, 1520, 1100, 1200]
tick_9 = [1200, 1750, 1050, 1100]
tick_10 = [1100, 1480, 1100, 1190]
tick_11 = [1190, 1650, 420, 420]
tick_12 = [420, 930, 420, 580]

print(decision_maker(tick_1, None))
print(decision_maker(tick_2, None))
print(decision_maker(tick_3, None))
print(decision_maker(tick_4, None))
print(decision_maker(tick_5, None))
print(decision_maker(tick_6, None))
print(decision_maker(tick_7, None))
print(decision_maker(tick_8, None))
print(decision_maker(tick_9, None))
print(decision_maker(tick_10, None))
print(decision_maker(tick_11, 2.38)) #1000 UDS = 1000/420 BTC = 2.38 BTC
#print(decision_maker(tick_12))
