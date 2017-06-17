
# coding: utf-8

# In[ ]:


dep_city = 'DAL'
arr_city = 'HOU'
dep_time = ['0600','0600','0606']

if (dep_city == 'DAL' and arr_city == "AUS") or (dep_city == 'AUS' and arr_city == "DAL"):
    travel_time = 50
elif (dep_city == 'AUS' and arr_city == "HOU") or (dep_city == 'HOU' and arr_city == "AUS"):
    travel_time = 45
else:
    travel_time = 65
    print(dep_city)
print(dep_time)
arrival_tim_1 = []
for each in dep_time:
    print(each)
    dep_time_mid = (int(each[:2])*60) + int(each[2:])
    print(dep_time_mid)
    while (dep_time_mid >=360 and dep_time_mid <=1320):
        arrival_time = dep_time_mid + travel_time 
        dep_time_mid = dep_time_mid + travel_time 
        arrival_tim_1.append(str(int(arrival_time / 60)).zfill(2) + str(arrival_time % 60).zfill(2))
print(arrival_tim_1)



# In[131]:

dep_city = 'AUS'
arr_city = 'DAL'
dep_time = ['0600','0700']

if (dep_city == 'DAL' and arr_city == "AUS") or (dep_city == 'AUS' and arr_city == "DAL"):
    travel_time = 50
elif (dep_city == 'AUS' and arr_city == "HOU") or (dep_city == 'HOU' and arr_city == "AUS"):
    travel_time = 45
else:
    travel_time = 65
if (arr_city == 'HOU'):
    ground_time = 35
elif (arr_city == 'DAL'):
    ground_time = 30
else: 
    ground_time = 25
arrival_tim_1 = []
for each in dep_time:
    dep_time_mid = (int(each[:2])*60) + int(each[2:])
    while (dep_time_mid >=360 and dep_time_mid <=1320-travel_time):
        arrival_time = dep_time_mid + travel_time
        arrival_tim_1.append(str(int(arrival_time / 60)).zfill(2) + str(arrival_time % 60).zfill(2))
        dep_time_mid = arrival_time + ground_time
        print(arrival_time)
print(dep_city, arr_city, arrival_tim_1)


# In[11]:

dep_city = ["DAL","HOU","AUS"]
arr_city = ["DAL","HOU","AUS"]
dep_time = ['0600','0700','0600']
for x in dep_city:
    for y in arr_city:
        if x == y:
            print("")
        else:
            if (x == 'DAL' and y == "AUS") or (x == 'AUS' and y == "DAL"):
                travel_time = 50
                print(x,y,travel_time)
            elif (x == 'AUS' and y == "HOU") or (x == 'HOU' and y == "AUS"):
                travel_time = 45
                print(x,y,travel_time)
            else:
                travel_time = 65
                print(x,y,travel_time)
            if (y == 'HOU'):
                ground_time = 35
                print(x,y,travel_time,ground_time)
            elif (y == 'DAL'):
                ground_time = 30
                print(x,y,travel_time,ground_time)
            else: 
                ground_time = 25
                print(x,y,travel_time,ground_time)
            arrival_tim_1 = []
            for each in dep_time:
                dep_time_mid = (int(each[:2])*60) + int(each[2:])
                while (dep_time_mid >=360 and dep_time_mid <=1320-travel_time):
                    arrival_time = dep_time_mid + travel_time
                    arrival_tim_1.append(str(int(arrival_time / 60)).zfill(2) + str(arrival_time % 60).zfill(2))
                    dep_time_mid = arrival_time + ground_time
                print(arrival_time)
            print(dep_city, arr_city, arrival_tim_1)
        


# In[25]:


div1 = ["Lions", "Tigers", "Jaguars", "Cougars"]
div2 = ["Whales", "Sharks", "Piranhas", "Alligators"]
div3 = ["Cubs", "Kittens", "Puppies", "Calfs"]

def create_schedule(list):
    """ Create a schedule for the teams in the list and return it"""
    s = []

    if len(list) % 2 == 1: list = list + ["BYE"]

    for i in range(len(list)-1):

        mid = len(list)/2
        l1 = list[:int(mid)]
        l2 = list[int(mid):]
        l2.reverse()	
    
        # Switch sides after each round
        if(i % 2 == 1):
            s = s + [ zip(l1, l2) ]
        else:
            s = s + [ zip(l2, l1) ]

        list.insert(1, list.pop())

    return s


def main():
    for round in create_schedule(div1):
        for match in round:
            print(match[0] + " - " + match[1])
    print
    for round in create_schedule(div2):
        for match in round:
            print(match[0] + " - " + match[1])
    print
    for round in create_schedule(div3): 
        for match in round:
            print(match[0] + " - " + match[1])
    print
    for round in create_schedule(div1+div2+div3): 
        for match in round:
            print(match[0] + " - " + match[1])
        print


if __name__ == "__main__":
    main()


# In[36]:

dep_city = ['DAL','HOU','AUS']

def roundrobin(list):
    s = []
    



if __name__ == "__main__":
    main()


# In[321]:



def create_schedule(list,list1,dep_time):
    i = 0 
    j = 0
    s = []
    
    for x in range(len(list)):
        if i < 2:
            i = i+1;
            
            flight_No = list1
            xx = list[i-1]
            yy = list[i]
            #print(flight_No)
            travel_time, ground_time = schedule_allocation(flight_No,xx,yy,dep_time)
            #print(flight_No, xx,yy,travel_time, ground_time)
            
            if list1 == 'T1':
                arr_time = dep_time + travel_time
                dep_time = arr_time + ground_time
                print(flight_No, xx,yy,arr_time,dep_time)
            elif list1 == 'T2':
                arr_time = dep_time + travel_time
                dep_time = arr_time + ground_time
                print(flight_No, xx,yy,arr_time,dep_time)
            elif list1 == 'T3':
                arr_time = dep_time + travel_time
                dep_time = arr_time + ground_time
                print(flight_No, xx,yy,arr_time,dep_time)
        else:
            i = 0;
            
            flight_No = list1
            xx = list[i-1]
            yy = list[i]
            #print(flight_No)
            
            travel_time, ground_time = schedule_allocation(flight_No,xx,yy,dep_time)
            #print(flight_No, xx,yy,travel_time, ground_time)
            
            if list1 == 'T1':
                
                arr_time = dep_time + travel_time
                dep_time = arr_time + ground_time
                print(flight_No, xx,yy,arr_time,dep_time)
            elif list1 == 'T2':
                arr_time = dep_time + travel_time
                dep_time = arr_time + ground_time
                print(flight_No, xx,yy,arr_time,dep_time)
            elif list1 == 'T3':
                arr_time = dep_time + travel_time
                dep_time = arr_time + ground_time
                print(flight_No, xx,yy,arr_time,dep_time)
            

def schedule_allocation(flight_No,dep_city,arr_city,dep_time):
    
    if (dep_city == 'DAL' and arr_city == "AUS") or (dep_city == 'AUS' and arr_city == "DAL"):
        if(arr_city == 'DAL'):
            ground_time = 30
        else:
            ground_time = 25
        travel_time = 50
        return(travel_time,ground_time)
    elif (dep_city == 'AUS' and arr_city == "HOU") or (dep_city == 'HOU' and arr_city == "AUS"):
        if(arr_city == 'AUS'):
            ground_time = 25
        else:
            ground_time = 35
        travel_time = 45
        return(travel_time,ground_time)     
    else:
        if(arr_city == 'DAL'):
            ground_time = 30
        else:
            ground_time = 35
        travel_time = 65
        return(travel_time,ground_time)
    
        #return(travel_time, ground_time)
    
        
def main():
    city = ['AUS','HOU','DAL']
    Flights = ['T1', 'T2', 'T3','T4', 'T5','T6']
    i = 0
    dep_time = 360
    terminal = [1,2,3]
    if terminal[0] == 1 and terminal[1] == 2 and terminal[2] == 3:
        i = 0
        for each in city:
            if each == city[0]:
                city = [city[1],city[2],city[0]]
                for y in range(1,4):
                    create_schedule(city,Flights[i],dep_time)
            i = i+1
            
    else:
        print("have to change the logic")
  
if __name__ == "__main__":
    main()      


# In[ ]:

div = ['AUS','HOU','DAL']
if div[0] == 'AUS':
    div = [div[1],div[2],div[0]]
    create_schedule(div1,lis1)
    print(div)
if div[0] == 'HOU':
    div = [div[1],div[2],div[0]]
    print(div)
if div[0] == 'DAL':
    div = [div[1],div[2],div[0]]
    print(div)


# In[255]:

div = ['DAL','HOU','AUS']
i = 0
terminal = [1,2,3]
if terminal[0] == 1 and terminal[1] == 2 and terminal[2] == 3:
    
    
    
        i = 0
        for each in div:
            
            if each == div[0]:
                div = [div[1],div[2],div[0]]
                dep = [div[2],div[0],div[1]]
                arr = [div[1],div[2],div[0]]
                
                print(div)
                print(dep)
                print(arr)
                
                
            for y in range(1,4):
                create_schedule(div,lis4[i],dep_time)
            i = i + 1    
               
            
           


# In[821]:

flight_No = "T1"
xx = "AUS"
yy = "HOU"
dep_time = 360
arr_time = 0

def schedule_allocation(flight_No,x,y):
    if (x == 'DAL' and y == "AUS") or (x == 'AUS' and y == "DAL"):
        travel_time = 50
        arr_time = dep_time + travel_time
        print(x,y,travel_time,arr_time)
    elif (x == 'AUS' and y == "HOU") or (x == 'HOU' and y == "AUS"):
        travel_time = 45
        arr_time = dep_time + travel_time
        print(x,y,travel_time,arr_time)
    else:
        travel_time = 65
        arr_time = dep_time + travel_time
        print(x,y,travel_time,arr_time)
    if (y == 'HOU'):
        ground_time = 35
        print(x,y,travel_time,ground_time,arr_time)
    elif (y == 'DAL'):
        ground_time = 30
        print(x,y,travel_time,ground_time,arr_time)
    else: 
        ground_time = 25
        print(x,y,travel_time,ground_time,arr_time)

  

schedule_allocation(flight_No,xx,yy)


# In[898]:

def main_logic(each,dep_city,arr_city):
    dep_time = 360
    arr_time = 0
    travel_time = 0
    ground_time = 0 
    i = 0
    while dep_time >= 360 and dep_time < 1320:
        if(dep_time < 1320 - ground_time- travel_time):
            if (dep_city[i] == "DAL" and arr_city[i] == "AUS") or (dep_city[i] == "AUS" and arr_city[i] == "DAL"):
                if(arr_city == "AUS"):
                    ground_time = 30
                else:
                    ground_time = 25
                    travel_time = 50
                    arr_time = dep_time + travel_time
                    dep_tim_1 = (str(int(dep_time / 60)).zfill(2) + str(dep_time % 60).zfill(2))
                    arrival_tim_1 = (str(int(arr_time / 60)).zfill(2) + str(arr_time % 60).zfill(2))
                    print(each,dep_city[i],arr_city[i],dep_tim_1,arrival_tim_1)
                    dep_time = arr_time + ground_time
                    if dep_city[2] == "DAL":
                        i = 0
                    else:
                        i = i + 1
        else:
            break
        if(dep_time < 1320 - ground_time - travel_time):
            if (dep_city[i] == "AUS" and arr_city[i] == "HOU") or (dep_city[i] == "HOU" and arr_city[i] == "AUS"):
                if(arr_city == "HOU"):
                    ground_time = 25
                else:
                    ground_time = 35
                    travel_time = 45
                    arr_time = dep_time + travel_time
                    dep_tim_1 = (str(int(dep_time / 60)).zfill(2) + str(dep_time % 60).zfill(2))
                    arrival_tim_1 = (str(int(arr_time / 60)).zfill(2) + str(arr_time % 60).zfill(2))
                    print(each,dep_city[i],arr_city[i],dep_tim_1,arrival_tim_1)
                    dep_time = arr_time + ground_time
                    if dep_city[2] == "AUS":
                        i = 0
                    else:
                        i = i + 1
        else:
            break
        if(dep_time < 1320 - ground_time - travel_time):
            if (dep_city[i] == "HOU" and arr_city[i] == "DAL") or (dep_city[i] == "DAL" and arr_city[i] == "HOU"):
                if(arr_city == "DAL"):
                    ground_time = 35
                else:
                    ground_time = 30
                    travel_time = 65
                    arr_time = dep_time + travel_time
                    dep_tim_1 = (str(int(dep_time / 60)).zfill(2) + str(dep_time % 60).zfill(2))
                    arrival_tim_1 = (str(int(arr_time / 60)).zfill(2) + str(arr_time % 60).zfill(2))
                    print(each,dep_city[i],arr_city[i],dep_tim_1,arrival_tim_1)
                    dep_time = arr_time + ground_time
                    if dep_city[2] == "HOU":
                        i = 0
                    else:
                        i = i + 1
        else:
            break



# In[927]:

city = ['AUS','HOU','DAL']
flights = ["T1","T2","T3","T4","T5","T6"]
Terminals = [1,2,3]
if Terminals[0] == 1 and Terminals[1] == 2 and Terminals[2] == 3:
    for each in flights:
        if each == "T1" or each == "T2" or each == "T3":
            j = 0
            arr_city = [city[j+1],city[j+2],city[j]]
            dep_city = [city[j],city[j+1],city[j+2]]
            city = [city[j+1],city[j+2],city[j]]
            print(dep_city)
            print(arr_city)
            main_logic(each,dep_city,arr_city)
        second_order = ["HOU","DAL"]
        if each == "T4" or each == "T5" or each == "T6":
            print(second_order)


# In[1018]:

def second(dep_city,arr_city):
    dep_time = 360
    arr_time = 0
    travel_time = 0
    ground_time = 0 
    i = 0
    while dep_time >= 360 and dep_time <= 1320:
        if (dep_city[i] == "HOU" and arr_city[i] == "DAL"):
                if(arr_city == "DAL"):
                    ground_time = 35
                else:
                    ground_time = 30
                    travel_time = 65
                    arr_time = dep_time + travel_time
                    print(dep_city[i],arr_city[i],dep_time,arr_time)
                    dep_time = arr_time + ground_time
                    if dep_city[1] == "HOU":
                        i = 0
                    else:
                        i = i + 1

        if (dep_city[i] == "DAL" and arr_city[i] == "HOU"):
                if(arr_city == "HOU"):
                    ground_time = 30
                else:
                    ground_time = 35
                    travel_time = 65
                    arr_time = dep_time + travel_time
                    print(dep_city[i],arr_city[i],dep_time,arr_time)
                    dep_time = arr_time + ground_time
                    if dep_city[1] == "DAL":
                        i = 0
                    else:
                        i = i + 1
        else:
            print(each)

dep_city = ["HOU","DAL"]
arr_city = ["DAL","HOU"]
dep_city_1 = ["DAL","HOU"]
arr_city_1 = ["HOU","DAL"]
terminal = ["T1"]
second(dep_city,arr_city)
second(dep_city_1,arr_city_1)


# In[1049]:

x = "HOU"
y = "DAL"
dep_time = 360
arr_time = 0
A = "DAL"
B = "HOU"
dep_time_1 = 360
arr_time_1 = 0
s = ["T4","T5","T6","T4","T5","T6","T4","T5","T6","T4","T5","T6","T4","T5","T6","T4","T5","T6","T4","T5","T6","T4","T5","T6"]
i = 0
while dep_time >= 360 and dep_time <= 1200:
    if (x == "HOU" and y == "DAL") :
        travel_time = 65
        ground_time = 30
    arr_time = dep_time + travel_time
    print(s[i],x,y,dep_time,arr_time)
    i =i+1
    dep_time = dep_time + travel_time + ground_time
    if (A == "DAL" and B == "HOU") :
        travel_time = 65
        ground_time = 35
    arr_time_1 = dep_time_1 + travel_time
    print(s[i],A,B,dep_time_1,arr_time_1)
    dep_time_1 = dep_time_1 + travel_time + ground_time
    i = i + 1
    


# In[ ]:



