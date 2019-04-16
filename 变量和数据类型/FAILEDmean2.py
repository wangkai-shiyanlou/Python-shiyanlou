N=int(input())
ls=input().split()
ls_avr=[]
ls_str=[]
 
for i in ls:
    try:
        if eval(i)>=-1000 and eval(i)<=1000 and eval(i)==round(eval(i),2):
            ls_avr.append(eval(i))              
        else:
            ls_str.append(i)
    except:
        ls_str.append(i)
 
for i in ls_str:
    print('ERROR: {} is not a legal number'.format(i))
summ=0
s=len(ls_avr)
for i in ls_avr:
    summ+=i
if s==0:
    print('The average of 0 numbers is Undefined')
 
elif s==1:
    Y=summ/s
    print('The average of 1 number is {:.2f}'.format(Y))
else:
    Y=summ/s
    print('The average of {} numbers is {:.2f}'.format(s,Y))
