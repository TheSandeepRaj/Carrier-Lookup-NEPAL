import re

# +977-985******* Nepal Telecom
# +977-986******* Nepal Telecom
# +977-984******* Nepal Telecom 
# +977-980******* Ncell 
# +977-981******* Ncell
# +977-982******* Ncell
# +977-961******* SmartCell 
# +977-962******* SmartCell 
# +977-988******* SmartCell
# 972 CDMA UTL 974/975	 CDMA	Sky SIM / Ntc CDMA
# not_ToDo:   963 Hello Nepal GSM  not in operation
# ToDo:  and whether the number is CDMA or GSM

user_details = input("Hey! Enter the mobile number?\n")

def carrier_detect(carrier):
    carrier = int(carrier)
    if (carrier == 980) or (carrier == 981) or (carrier == 982) :       #ToDo 9801 &9820 are Pro others are Prepaid
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