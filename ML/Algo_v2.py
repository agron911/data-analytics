#!/usr/bin/env python
# coding: utf-8

# ### binary search

# In[1]:


def binary_search(lis,item):
    low = 0
    high = len(lis)-1
    
    while low <= high:
        mid = int((low+high)/2)
        guess = lis[mid]
        if guess<item:
            low = mid+1
        elif guess ==item:
            return mid
        else:
            high = mid -1
            
    return None
my_list = [1,3,5,7,9]
print(binary_search(my_list,7))


# 
# ### Selection sort
# 

# In[2]:




def findSmallest(arr):
    smallest = arr[0]
    index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index =i
            
    return index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest =  findSmallest(arr)
        
        newArr.append(arr.pop(smallest))
    return newArr

selectionSort([5,3,6,2,10])


# ### recursive

# In[9]:


def summ(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return arr[0]+sum(arr[1:])
    
summ([1,2,3,4])


# In[19]:


import numpy as np
def maxx(arr):
    if len(arr)==2:
        return arr[0] if arr[0]>arr[1] else arr[1]
    sub_arr = arr[1:]
    return arr[0] if (arr[0] > np.array(sub_arr)).any() else maxx(sub_arr)
maxx([1,2,3,4,5])


# In[11]:


max([1,2,3,4,5])


# In[83]:


def bs(arr,left,right,num):
    middle = int((left+right)/2)
    
    if left>right:
        return -1
    
    if arr[middle]==num:
        return middle
    elif num>arr[middle]:

        return bs(arr,middle+1,right,num)
    elif num<arr[middle]:
        return bs(arr,left,middle-1,num)
    

arr =[1,2,3,5,6,8,11]
(left, right) =(0, len(arr)-1)
bs(arr,left,right,5)


# In[25]:


a=[0,1,2,3,4,5]
a[:3]


# ### Quicksort 
# 

# In[168]:


def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot =arr[0]
        left_arr = []
        right_arr =[]
        result=[]
        for i in arr[1:]:
            if pivot>i:
                left_arr.append(i)
            else:
                right_arr.append(i)
        left_arr.append(pivot)
        left_arr=quicksort(left_arr)
        right_arr=quicksort(right_arr)
        
       
        return left_arr+right_arr
print('cpu',psutil.cpu_percent(interval=0.3))
    
quicksort([33,10,15,1,55,30])


# In[164]:


def quickSort_2(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i<pivot]
        greater = [i for i in arr[1:] if i>pivot]
        return quickSort_2(less)+ [pivot]+quickSort_2(greater)
    
print('cpu',psutil.cpu_percent(interval=0.3))
quicksort([33,10,15,1,55,30])


# ## Coursera automating real world task

# In[1]:


import requests


# In[3]:


response = requests.get('https://www.google.com')


# In[12]:


response.content


# In[13]:


response.ok


# In[19]:


type(response)


# In[20]:


if not response.ok:
    raise Exception("Get failed with statue code {}".format(response.status_code))


# In[23]:


url = 'https://google.com/search'
q={
    'q':'cool'
}
response = requests.get(url,params=q)


# In[24]:


response.request.url


# In[33]:


p  ={
    'description':'cool'
}
response = requests.post(url,data=p)


# In[32]:


response.request.body # json=p


# In[34]:


response.request.body # data =p


# In[63]:


import os 
path = os.getcwd()
for entry in os.listdir(path+'\\txt'):
#     if os.path.isdir(os.path.join(path,entry)):
#         print(entry)
#         pass
   
    if os.path.isfile(os.path.join(path+'\\txt',entry)):
        print(entry)
        with open(path+'\\txt\\'+entry) as txt:
            content=txt.read()
            print(content)


# ### Hash table
# 

# In[3]:


def all_one(x):
    return 1
all_one(123)


# In[9]:


import random
def rand_(x):
    return random.random()
rand_(123)


# In[12]:


voted={}
def vote(name):
    if voted.get(name):
        print('You voted! Please leave.')
    else:
        voted[name]=True
        print('{}, vote success'.format(name))

vote('tom')
vote('tom')


# In[2]:


# from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np 

# x1 = x2 = np.arange(-5,15,1)
# x1,x2 =np.meshgrid(x1,x2)

# z = 1/2*x1**2

# plt.ion()
# for i in range(30000):
#     plt.clf()
#     fig = plt.gcf()
#     ax = fig.gca(projection='3d')
#     ax.plot_surface(x1,x2,z,cmap='rainbow')
#     plt.pause(0.001)
#     plt.ioff()
    
#     z=  z-x1+2*x2
    
# plt.show()


# ## EMAIL
# 

# In[15]:


from email.message import EmailMessage
from email.mime.text import MIMEText
import smtplib
message = EmailMessage()
message


# In[17]:


sender = 'chtsais@vis.com.tw'
recipent = 'chtsais@vis.com.tw'
message['From']=sender
message['To'] = recipent
print(message)


# In[18]:


message['Subject'] = 'Greeting from coursera auto test'
print(message)


# In[19]:


body = """ Hey this is a test from python mail package """
message.set_content(body)


# In[20]:


print(message)


# In[23]:



# message.attach(MIMEText('automation IT','plain','utf-8'))
s = smtplib.SMTP('10.1.254.112')
s.send_message(message)
s.quit()


# In[35]:


import os
import os.path as path
import mimetypes


# In[37]:


cwd = os.getcwd()
p = cwd+ '\\txt\\'
os.listdir(p)
attach_p = p+'device.png'
attach_n = path.basename(attach_p)
mime_type, _ = mimetypes.guess_type(attach_p)
print(mime_type)


# In[39]:


mime_type, mime_subtype = mime_type.split('/',1)
print(mime_type)
mime_subtype


# In[41]:


with open(attach_p,'rb') as ap:
    message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attach_n)

print(message)


# In[76]:


from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate('report2.pdf')


# In[77]:


from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()


# In[78]:


report_title = Paragraph("A  Complete Inventory of My Fruit",styles['h1'])
report.build([report_title])


# In[79]:


fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

table_d=[]
for k,v in fruit.items():
    table_d.append([k,v])
table_d


# In[81]:


report_table = Table(data = table_d)
report.build([report_title,report_table])


# In[99]:


from reportlab.lib import colors
table_styles = [('GRID',(0,0),(0,7),1, colors.black)]
report_table = Table(data = table_d, style = table_styles,hAlign='LEFT')
report.build([report_title, report_table])


# In[105]:


from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
report_pie = Pie(width=100, height = 100)

report_pie.data=[]
report_pie.labels=[]
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_pie


# In[106]:


report_chart = Drawing()
report_chart.add(report_pie)


# In[107]:


report.build([report_title, report_table,report_chart])


# ## BFS

# In[25]:


graph = {}
graph["you"] = ['alice', 'bob', 'claire']
graph["bob"] = ['anuj', 'peggy']
graph["alice"] = ['peggy']
graph["claire"] = ['thom','jonny']
graph['anuj']=[]
graph['peggy']=['you','jonny']
graph['thom']=['peggy']
graph['jonny']=['peggy']

from collections import deque


# In[39]:



def person_is_seller(name):
    return name[-1] =='y'
def search(name):
    search_queue = deque()
    search_queue +=graph[name]
    searched=[]
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person+' is a mango seller!')
               
            else:
                search_queue +=graph[person]
        searched.append(person)
        
    
search('you')


# In[40]:


routine={}
routine['Wake up'] = []
routine['Shower'] = ['Wake up']
routine['Brush teeth'] = ['Wake up']
routine['Eat breakfast'] = ['Brush teeth']


# ### Matrix chain multiplication
# 
# 

# In[46]:


def mult(chain):
    n = len(chain)
    
    aux = {(i,i):(0,) + chain[i] for i in range(n)}
    print(aux)
    
    for i in range(1,n):
        for j in range(0, n-i):
            best = float('inf')
            print(best,'\n')
            
            for k in range(j,j+i):
                print('i:',i,'j:{} '.format(k),'k:{}\n'.format(k))
mult([('A',10,20), ('B',20,30), ('C',30,40)])


# In[47]:


phone_book = {}
phone_book['Jane'] = '415 567 3579'

print(phone_book)


# In[62]:


voted ={}
voted.get('tom')


# In[64]:


def check_voter(name):
    if voted.get(name):
        print('kick')
    else:
        voted[name]=True
        print('success')
check_voter('tom')
check_voter('to')


# In[65]:


cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data


# In[68]:


import libvirt-python-7.10.0


# In[77]:


import psutil
psutil.cpu_count(logical=True)


# In[78]:


psutil.virtual_memory()


# ## Dijkstra algo

# In[37]:


graph ={}
graph['start']={}
graph['start']['a']=6
graph['start']['b']=2
graph['a'] ={}
graph['a']['Fin']=1
graph['b']={}
graph['b']['a']=3
graph['b']['Fin']=5
graph['Fin']={}
infinity = float('inf')
costs = {}
costs['a']=6
costs['b']=2
costs['Fin'] = infinity
parents ={}
parents['a']= 'start'
parents['b']= 'start'
parents['fin'] = None
processed=[]
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node=None
    for node in costs:
        cost = costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
node = find_lowest_cost_node(costs)


while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] >new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    print(node)


# In[38]:


print(cost)


# In[39]:


parents


# In[41]:


g2 ={}
g2['start']={}
g2['start']['a']=5
g2['start']['b']=2

g2['a']={}
g2['a']['c']=4
g2['a']['d']=2

g2['b']={}
g2['b']['a']=8
g2['b']['d']=7

g2['c']={}
g2['c']['fin']=3
g2['c']['d']=6

g2['d']={}
g2['d']['fin']=1

g2['fin']={}

costs = {}
infinity = float('inf')
costs['a']=5
costs['b']=2
costs['c']=infinity
costs['d']=infinity
costs['fin']=infinity

parents ={}
parents['a']='start'
parents['b']='start'
parents['c']={}
parents['d']={}
parents['fin']={}

processed =[]
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node=None
    for node in costs:
        cost = costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
node = find_lowest_cost_node(costs)


while node is not None:
    cost = costs[node]
    neighbors = g2[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] >new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    print(node)

# def find_lowest_cost(costs):
#     lowest_cost = infinity
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_code = cost
#             lowest_cost_node = node
#     return lowest_cost_node

# node = find_lowest_cost(costs)

# while node is not None:
#     cost = costs[node]
#     neighbors = g2[node]
#     for n in neighbors.keys():
#         new_cost = cost+ neighbors[n]
#         if new_cost < costs[n]:
#             costs[n] = new_cost
#             parents[n] = node
#     processed.append(node)
#     node = find_lowest_cost(costs)
    


# In[44]:


print(costs['fin'])


# In[43]:


parents


# In[45]:


graph = {}
graph['start'] = {}
graph['start']['a']=10

graph['a']={}
graph['a']['b']=20
graph['b']={}
graph['b']['c']=1
graph['b']['fin'] = 30
graph['c']={}
graph['c']['fin']=1

graph['fin']={}

infinity = float('inf')

costs = {}
costs['a']=10
costs['b']=infinity
costs['c']=infinity
costs['fin']=infinity

parents={}
parents['a']='start'
parents['b']={}
parents['c']={}
parents['fin']={}

processed = []

def lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for n in costs:
        cost = costs[n]
        if n not in processed and cost< lowest_cost:
            lowest_cost = cost
            lowest_cost_node = n
    return lowest_cost_node
    


node = lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n]> new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = lowest_cost_node(costs)


# In[46]:


parents


# In[47]:


costs['fin']


# ## Set-covering problem

# In[137]:


states_needed = set(['mt','wa','or','id','nv','ut','ca','az'])
stations ={}
stations['kone'] = set(['id','nv','ut'])
stations['ktwo'] = set(['wa','id','mt'])
stations['kthree'] = set(['or','nv','ca'])
stations['kfour'] = set(['nv','ut'])
stations['kfive'] = set(['ca','az'])

final_stations = set()

best_station = None


# In[138]:



states_covered = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
      
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered
    print(final_stations)


# In[140]:


final_stations


# In[141]:


print(final_stations)


# In[ ]:





# In[ ]:




