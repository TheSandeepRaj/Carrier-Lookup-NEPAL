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
# ToDo: 972 CDMA UTL    963 Hello mobile / Nepal Satellite Telecom      974/975	 CDMA	Sky SIM / Ntc CDMA

user_details = input("Hey! Enter the mobile number?\n")

def carrier_detect(carrier):
    carrier = int(carrier)
    if (carrier == 980) or (carrier == 981) or (carrier == 982) :
        return 'Ncell'

    elif (carrier == 984) or (carrier == 986):
        return 'Nepal Telecom (Pre-Paid)'

    elif (carrier == 985):
        return 'Nepal Telecom (Post-Paid)'

    elif (carrier == 961) or (carrier == 962) or (carrier == 988) :
       return'SmartCell'
    
    else:
        print("Sorry we couldn't find your carrier info.")
        exit()
        
phone_num_regex = re.compile(r'(\+)?(\d\d\d)?(-)?(\d\d\d)(\d\d\d\d\d\d\d)')
num = phone_num_regex.search(user_details)

carrier_part = num.group(4)
number_only = num.group(4) + num.group(5)

print('Carrier of number '+ number_only + ' is "' + carrier_detect(carrier_part) + '".')