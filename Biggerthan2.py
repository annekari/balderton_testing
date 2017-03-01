



def validate_numbers(hours, rate):
   validate = False

   try:
       hours = float(hours)
       rate = float(rate)
       pay = hours*rate
       validate = True

   except:
       hours = raw_input('Enter Hours as a number :')
       rate = raw_input('Enter Rate as a number :')
       hours = float(hours)

       if (hours > 0 and rate > 0 ) :
           validate = True
           print "Nice work, your hours and rate is stored as :", hours, rate
       else:
           print ' hours and rate is not put in as a number'
   return validate

def overtime(hours, rate) :
    overtime = 0
    validate = validate_numbers(hours, rate)
    hours = float(hours)
    rate = float(rate)
    
    if (hours > 40 ):
        overtime = hours - 40.0
        overtime = overtime * rate * 1.5
      
    else:
        print 'No overtime payment achieved'
            
    return overtime

def computepay (hours, rate) :
    pay = 0
    validate = validate_numbers(hours,rate)

    if (hours >= 40):
        pay = 40 * float(rate)
        pay = pay + float(overtime(hours,rate))
    else:
        pay = hours * rate
    
    return pay

while True:

    print "Let's compute your pay "

    hours = raw_input('Enter Hours :')
    rate = raw_input('Enter Rate :')
    pay = -1.0

    if(validate_numbers(hours,rate)):
        print "Pay :", computepay(hours, rate)
        line = raw_input('Write Done if you want to quit and Con if you want to run the script again : ')

        print "Let's quit: ", line
    else:
        print " Enter Hours and Rate as a number"

    if(line=='Done'):
        break




	

	