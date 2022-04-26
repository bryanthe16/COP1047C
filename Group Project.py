import sys
equationType = input('Please enter what type of equation you would like to use by typing "Force" or "Speed": ')

#defining inputs for variables in the force equation and defining the units for each variable
if equationType == 'Force':
    force = input('Please enter the force value or type "unknown" if you want to solve for it: ')
    mass = input('Please enter the mass value or type "unknown" if you want to solve for it: ')
    acceleration = input('Please enter the acceleration value or type "unknown" if you want to solve for it: ')
    # error code for if more than one unknown value is specified. It then exits the program.
    if (force == 'unknown' and mass == 'unknown') or (force == 'unknown' and acceleration == 'unknown') or (mass == 'unknown' and acceleration == 'unknown'):
        print('Only one variable can be solved for. Please re-enter your values.')
        exit()

    if equationType == 'Force':
        unitF = input('Please enter the unit of force you would like (type "N" for Newtons): ')
        unitM = input('Please enter the unit of mass you would like (type "g" for grams, and "kg" for kilograms): ')
        unitA = input('Please enter the unit of acceleration you would like (type "ms" for meters per second squared or "kms" '
                    'for kilometers per second squared): ')
        # error code for if the units are invalid. It then exits the program.
        if (unitF != 'N' and unitM != 'g' and unitA != 'ms') or (unitF != 'N' and unitM != 'g' and unitA != 'kms') or (unitF != 'N' and unitM != 'kg' and unitA != 'ms') or (unitF != 'N' and unitM != 'kg' and unitA != 'kms'):
            print('Please enter a valid unit and make sure that you have entered valid inputs.')
            exit()
    #calculations if the user wants to solve for force
    if force == 'unknown' and unitM == 'kg' and unitA == 'ms' and unitF == 'N':
        force = float(mass) * float(acceleration)
        print('The force is equal to'+ ' ' + str(force) + ' '+ 'Newtons.')
    elif force == 'unknown' and unitM == 'g' and unitA == 'ms' and unitF == 'N':
        force = (float(mass) * float(acceleration)) / 1000
        print('The force is equal to'+ ' ' + str(force) + ' '+ 'Newtons.')
    elif force == 'unknown' and unitM == 'kg' and unitA == 'kms' and unitF == 'N':
        force = (float(mass)*float(acceleration)) * 1000
        print('The force is equal to' + ' ' + str(force) + ' ' + 'Newtons.')
    elif force == 'unknown' and unitM == 'g' and unitA == 'kms'and unitF == 'N':
        force = float(mass)*float(acceleration)
        print('The force is equal to' + ' ' + str(force) + ' ' + 'Newtons.')

    #Calculations if the user wants to solve for mass
    elif mass == 'unknown' and unitM =='g' and unitA == 'ms' and unitF == 'N':
        mass = (float(force)/float(acceleration)) * 1000
        print('The mass is equal to' + ' ' + str(mass) + ' ' + 'grams.')
    elif mass == 'unknown' and unitM == 'g' and unitA == 'kms' and unitF == 'N':
        mass = (float(force)/float(acceleration))
        print('The mass is equal to' + ' ' + str(mass) + ' ' + 'grams.')
    elif mass == 'unknown' and unitM == 'kg' and unitA == 'ms' and unitF == 'N':
        mass = (float(force)/float(acceleration))
        print('The mass is equal to' + ' ' + str(mass) + ' ' + 'kilograms.')
    elif mass == 'unknown' and unitM == 'kg' and unitA == 'kms' and unitF == 'N':
        mass = (float(force)/float(acceleration)) / 1000
        print('The mass is equal to' + ' ' + str(mass) + ' ' + 'kilograms.')

    #Calculations if the user wants to solve for acceleration
    elif acceleration == 'unknown' and unitM == 'g' and unitA == 'ms' and unitF == 'N':
        acceleration == (float(force)/float(mass)) * 1000
        print('The acceleration is equal to' + ' ' + str(acceleration) + ' ' + 'meters per second squared.')
    elif acceleration == 'unknown' and unitM == 'g' and unitA == 'kms' and unitF == 'N':
        acceleration = (float(force)/float(mass))
        print('The acceleration is equal to' + ' ' + str(acceleration) + ' ' + 'kilometers per second squared.')
    elif acceleration == 'unknown' and unitM == 'kg' and unitA == 'ms' and unitF == 'N':
        acceleration = (float(force)/float(mass))
        print('The acceleration is equal to' + ' ' + str(acceleration) + ' ' + 'meters per second squared.')
    elif acceleration == 'unknown' and unitM == 'kg' and unitA == 'kms' and unitF == 'N':
        acceleration = (float(force)/float(mass)) / 1000
        print('The acceleration is equal to' + ' ' + str(acceleration) + ' ' + 'kilometers per second squared.')

#defining inputs for variables in the speed equation and defining the units for each variable
elif equationType == 'Speed':
    speed = input('Please enter the speed value or type "unknown" if you want to solve for it: ')
    distance = input('Please enter the distance value or type "unknown" if you want to solve for it: ')
    time = input('Please enter the time value or type "unknown" if you want to solve for it: ')
    #error code for if more than one unknown value is specified. It then exits the program.
    if (speed == 'unknown' and distance == 'unknown') or (speed == 'unknown' and time == 'unknown') or (distance == 'unknown' and time == 'unknown'):
        print('Only one variable can be solved for. Please re-enter your values.')
        exit()

    if equationType == 'Speed':
        unitS = input('Please enter the unit of speed you would like (type "ms" for meters per second or "kph" for kilometers per hour): ')
        unitD = input('Please enter the unit of distance you would like (type "m" for meters, or "km" for kilometers): ')
        unitT = input('Please enter the unit of time you would like (type "s" for second or "h" for hour): ')
        #error code for if the units are invalid. It then exits the program.
        if (unitS != 'ms' and unitD != 'm' and unitT != 's') and (unitS != 'ms' and unitD != 'm' and unitT != 'h') and (unitS != 'kph' and unitD != 'm' and unitT != 's') and (unitS != 'kph' and unitD != 'm' and unitT != 'h') and (unitS != 'ms' and unitD != 'km' and unitT != 's') and (unitS != 'ms' and unitD != 'km' and unitT != 'h') and (unitS != 'kms' and unitD != 'km' and unitT != 's') and (unitS != 'kms' and unitD != 'km' and unitT != 'h'):
            print('Please enter a valid unit and make sure that you have entered valid inputs.')
            exit()

    #calculations if the user wants to solve for speed
    if speed == 'unknown' and unitS == 'ms' and unitD == 'm' and unitT == 's':
        speed = float(distance) / float(time)
        print('The speed is equal to'+ ' ' + str(speed) + ' '+ 'meters per second.')
    elif speed == 'unknown' and unitS == 'kph' and unitD == 'm' and unitT == 's':
        speed = (float(distance)/float(time)) * 3.6
        print('The speed is equal to'+ ' ' + str(speed) + ' '+ 'kilometers per hour.')
    elif speed == 'unknown' and unitS == 'ms' and unitD == 'km' and unitT == 's':
        speed = (float(distance)*1000) / float(time)
        print('The speed is equal to'+ ' ' + str(speed) + ' '+ 'meters per second.')
    elif speed == 'unknown' and unitS == 'kph' and unitD == 'km' and unitT == 's':
        speed = float(distance) / (float(time)/3600)
        print('The speed is equal to'+ ' ' + str(speed) + ' '+ 'kilometers per hour.')
    elif speed == 'unknown' and unitS == 'ms' and unitD == 'm' and unitT == 'h':
        speed = float(distance) / (float(time)*3600)
        print('The speed is equal to'+ ' ' + str(speed) + ' '+ 'meters per second.')
    elif speed == 'unknown' and unitS == 'kph' and unitD == 'm' and unitT == 'h':
        speed = (float(distance)/1000) / float(time)
        print('The speed is equal to'+ ' ' + str(speed) + ' '+ 'kilometers per hour.')
    elif speed == 'unknown' and unitS == 'ms' and unitD == 'km' and unitT == 'h':
        speed = (float(distance)/float(time)) / 3.6
        print('The speed is equal to'+ ' ' + str(speed) + ' '+ 'meters per second.')
    elif speed == 'unknown' and unitS == 'kph' and unitD == 'km' and unitT == 'h':
        speed = float(distance) / float(time)
        print('The speed is equal to'+ ' ' + str(speed) + ' '+ 'kilometers per hour.')

    #calculations if the user wants to solve for distance
    elif distance == 'unknown' and unitS == 'ms' and unitD == 'm' and unitT == 's':
        distance = float(speed) * float(time)
        print('The distance is equal to'+ ' ' + str(distance) + ' '+ 'meters.')
    elif distance == 'unknown' and unitS == 'kph' and unitD == 'm' and unitT == 's':
        distance = (float(speed)*3.6) * float(time)
        print('The distance is equal to'+ ' ' + str(distance) + ' '+ 'meters.')
    elif distance == 'unknown' and unitS == 'ms' and unitD == 'km' and unitT == 's':
        distance = (float(speed) * float(time)) / 1000
        print('The distance is equal to'+ ' ' + str(distance) + ' '+ 'kilometers.')
    elif distance == 'unknown' and unitS == 'kph' and unitD == 'km' and unitT == 's':
        distance = float(speed) * (float(time)/3600)
        print('The distance is equal to'+ ' ' + str(distance) + ' '+ 'kilometers.')
    elif distance == 'unknown' and unitS == 'ms' and unitD == 'm' and unitT == 'h':
        distance = float(speed) * (float(time)*3600)
        print('The distance is equal to'+ ' ' + str(distance) + ' '+ 'meters.')
    elif distance == 'unknown' and unitS == 'kph' and unitD == 'm' and unitT == 'h':
        distance = (float(speed) * float(time)) * 1000
        print('The distance is equal to'+ ' ' + str(distance) + ' '+ 'meters.')
    elif distance == 'unknown' and unitS == 'ms' and unitD == 'km' and unitT == 'h':
        distance = (float(speed)/3.6) * float(time)
        print('The distance is equal to'+ ' ' + str(distance) + ' '+ 'kilometers.')
    elif distance == 'unknown' and unitS == 'kph' and unitD == 'km' and unitT == 'h':
        distance = float(speed) * float(time)
        print('The distance is equal to'+ ' ' + str(distance) + ' '+ 'kilometers.')

    #calculations if the user wants to solve for time
    elif time == 'unknown' and unitS == 'ms' and unitD == 'm' and unitT == 's':
        time = float(distance) / float(speed)
        print('The time is equal to'+ ' ' + str(time) + ' '+ 'seconds.')
    elif time == 'unknown' and unitS == 'kph' and unitD == 'm' and unitT == 's':
        time = float(distance) / (float(speed)/3.6)
        print('The time is equal to'+ ' ' + str(time) + ' '+ 'seconds.')
    elif time == 'unknown' and unitS == 'ms' and unitD == 'km' and unitT == 's':
        time = (float(distance)*1000) / float(speed)
        print('The time is equal to'+ ' ' + str(time) + ' '+ 'seconds.')
    elif time == 'unknown' and unitS == 'kph' and unitD == 'km' and unitT == 's':
        time = (float(distance) / float(speed)) * 3600
        print('The time is equal to'+ ' ' + str(time) + ' '+ 'seconds.')
    elif time == 'unknown' and unitS == 'ms' and unitD == 'm' and unitT == 'h':
        time = (float(distance) / float(speed)) / 3600
        print('The time is equal to'+ ' ' + str(time) + ' '+ 'hours.')
    elif time == 'unknown' and unitS == 'kph' and unitD == 'm' and unitT == 'h':
        time = (float(distance)/1000) / float(speed)
        print('The time is equal to'+ ' ' + str(time) + ' '+ 'hours.')
    elif time == 'unknown' and unitS == 'ms' and unitD == 'km' and unitT == 'h':
        time = float(distance) / (float(speed)*3.6)
        print('The time is equal to'+ ' ' + str(time) + ' '+ 'hours.')
    elif time == 'unknown' and unitS == 'kph' and unitD == 'km' and unitT == 'h':
        time = float(distance) / float(speed)
        print('The time is equal to'+ ' ' + str(time) + ' '+ 'hours.')

#will close the program if something other than force or speed is typed
elif equationType != 'Force' or equationType != "Speed":
    print('Please enter a valid equation type.')

#in case an invalid string value or float number/integer is entered
else:
    print('Please recheck your values into the calculator (make sure you do not include spaces or unnecessary capitaliza'
          'tion nor units).')