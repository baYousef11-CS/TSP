import random
city=[]


for i in range(6):
    l1 = []
    for j in range(0, 6):
        r = random.randint(1,100)
        l1.append(r)
        if i==j:
            l1.pop(i)
            l1.insert(i,0)
    city.append(l1)






st=city[0][0]

def TSP_Path(c1,city):
    c1=c1
    path=[]
    path.append(c1)
    z=[]
    z.append(c1)
    for i in range(len(city)):
        if i==len(city)-1:
            r=0
            path.append(city[c1][r])
            break
        r = random.randint(0, len(city)-1)
        if r != c1 and r not in z:
            path.append(city[c1][r])
            c1 = r
            z.append(r)
        else:
            while r == c1:
                r = random.randint(0, len(city)-1)
            while r in z:
                r=random.randint(0,len(city)-1)
            path.append(city[c1][r])
            c1 = r
            z.append(r)
    return path




def road_distance(l):
    s=0
    for i in l:
        s+=i
    return s




population=[]
for i in range(3):
    population.append(TSP_Path(st,city))

array_dis=[]
for i in range(len(population)):
    array_dis.append(road_distance(population[i]))






cs=[]
new_x=[]
population_x=[[],[],[],[]]
for i in range(3):
    population_x[i].extend(population[i])
array_dis_x=array_dis


for i in range(10000):
    cs.clear()
    new_x.clear()
    r=random.randint(0,2)
    cs.extend(TSP_Path(st,city))
    if road_distance(cs)<array_dis_x[r]:
        population_x[-1].clear()
        population_x[-1].extend(cs)
        m=array_dis_x.index(max(array_dis_x))
        new_x.extend(TSP_Path(st,city))
        population_x[m].clear()
        population_x[m].extend(new_x)
        if len(array_dis_x)==3:
            array_dis_x.append(road_distance(cs))
        else:
            array_dis_x.pop()
            array_dis_x.append(road_distance(cs))





m=array_dis_x.index(min(array_dis_x))
path_x=[]
x=array_dis_x[m]
path_x.extend(population_x[m])

print("CITY:",city)

print("---------------------------------------------------\n")

print("Population:",population_x,"\n")
print("Fitness Function:",array_dis_x)

print("---------------------------------------------------\n")

print("X*:",path_x,"\n")
print("Fitness Value:",x)











