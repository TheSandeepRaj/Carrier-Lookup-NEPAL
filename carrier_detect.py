# Nepal Telecom +977-98(4/5/6)*******
# Ncell         +977-98(0/1/2)******* 
# SmartCell     +977-9(61/62/88)*******  
# UTL   	    +977-972*******  
# Sky by NTC    +977-97(4/5)*******   CDMA 
# TODO: input from file or type Option 
# 

import re

user_details = input("Hey! Enter the mobile number?\n")

def carrier_detect(carrier):
    carrier = int(carrier)
    if (carrier == 980) or (carrier == 981) or (carrier == 982) :       # TODO: 9801 &9820 are Pro others are Prepaid
        return 'Ncell', 'GSM'

    elif (carrier == 984) or (carrier == 986):
        return 'Nepal Telecom (Pre-Paid)','GSM'

    elif (carrier == 985):
        return 'Nepal Telecom (Post-Paid)', 'GSM'

    elif (carrier == 961) or (carrier == 962) or (carrier == 988) :
       return 'SmartCell', 'GSM'

    elif (carrier == 972) :
       return 'UTL', 'CDMA'

    elif (carrier == 974) or (carrier == 975) :
       return'Sky by NTC', 'CDMA'    #prepaid
    
    else:
        print("Sorry we couldn't find your carrier info.")
        exit()
        

phone_num_regex = re.compile(r'(\+)?(\d\d\d)?(-)?(\d\d\d)(\d\d\d\d\d\d\d)')
num = phone_num_regex.search(user_details)

carrier_part = num.group(4)
number_only = num.group(4) + num.group(5)

carrier, nw_tech = carrier_detect(carrier_part)
print('Carrier of number {} is {} and the given number uses {} technology.'.format(number_only, carrier, nw_tech) )