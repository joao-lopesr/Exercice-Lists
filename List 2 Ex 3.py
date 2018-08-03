def convert (hour, minute):
    if hour > 12:
        hour = hour - 12
        a = "P.M"

    elif hour < 12:
        a = "A.M"
    
    return [hour, minute, a]

while True:

    print ('Please insert an hour to convert it to A.M-P.M mode:')
    hour = int(input('Hour:'))
    minute = int(input('Minute:'))

    while not 0<hour or not hour<24 or not  0<minute or not 60>minute:
        hour = int(input('Please type a valid hour:'))
        minute = int(input('Please type a valid minute:'))

    time = convert(hour,minute)

    print (str(time[0])+':'+ str(time[1]) +' '+ time[2]) 
        
        

    

    
    


