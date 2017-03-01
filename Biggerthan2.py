# 
# hours = raw_input('Enter Hours :')
# rate = raw_input('Enter Rate :')
# pay = -1.0

def validate_numbers(hours, rate):
   validation = False 
   return True
    # try:
#     hours = float(hours)
#     rate = float(rate)
#     pay = hours*rate
#     valiate = True
#     except:
#     hours = raw_input('Enter Hours as a number :')
#     rate = raw_input('Enter Rate as a number :')
#     hours = float(hours)
      
# if (hours > 0 and rate > 0 ) :
#         validate = True 
#         print ' Nice work, your hours and rate is stored as :', hours, rate
# else:
#          print ' hours and rate is not put in as a number'
#     
    # return validation

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
    if (hours >= 40): 
        pay = 40 * float(rate)
        pay = pay + float(overtime (hours,rate))
    else:
        pay = hours * rate
    
    return pay

while True:
    line = raw_input('>')
    print 'line [0]: ', line[0]
    if(line[0]=='#'):
        continue
    if(line=='Done'):
        break
    print "blablabla", line
    
print 'Done'
 

# print 'Pay :', computepay(hours, rate)

# x=5
# if x > 2:
# 	print ' Bigger than 2'
# 	print ' still bigger '
# print 'Done with 2'
# 
# for i in range(5) :
# 	print i
# 	if i > 2 :
# 		print ' Bigger than 2 '
# 	print ' Done with i ', i
# print 'All Done' 



	

	