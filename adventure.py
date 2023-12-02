import sys;
import json;
from collections import namedtuple


filename = sys.argv[1]
       
with open(filename, 'r') as file:
    data = json.load(file)



# def mapDecoder(mapDict):
#     return namedtuple('X',mapDict.keys())(*mapDict.values())

user_inventory=[];


def read(ind):
     global map_object 
    #  map_object= mapDecoder(data[ind])
     map_object=data[ind]
  
    #  print(f'> {map_object[\'name\']}\n')
     print(map_object['name'])
     print(map_object['desc'])
     print()
     if('items' in map_object):
          print("Items:",end=" ")
          for item in map_object['items']:
            print(item,end=" ")
          print("\n")
     exits=map_object['exits']
     print("Exits:",end=" ")
     for key in exits:
            print(f'{key}',end=" ");
     print("\n")
        
def process():

        # print(type(data[0]))
       

        while(True):

            try:
                instruction=str(input("What would you like to do? "))
                instruction=instruction.lower();
                command=instruction.split(" ");

            except EOFError as e:
                print(f'Use \'quit\' to exit.')
                continue
            verb=command[0]     
            present=False
            item_found=False
            if(verb=="go"):
                if(len(command)<2):
                    print(f'Sorry, you need to \'{verb}\' somewhere.')
                    continue
                direction=command[1]
                exits=map_object['exits']
                for key in exits:
                    if(key==direction):
                       present=True
                       global value 
                       value=exits[key]
                       print(f'You go {direction}.\n')
                       read(value)

            if(verb=="go" and present==False):
                print(f'There\'s no way to go {direction}')
            
            if(verb=="look"):
                 read(value)
            
            if(verb=="get"):
                if(len(command)<2):
                    print(f'Sorry,What do you need to {verb}?')
                    continue
                if(hasattr(map_object,'items')):
                    item_to_get=command[1]
                    items=map_object['items']
                    for item in items:
                        if(item==item_to_get):
                            item_found=True
                            user_inventory.append(item)
                            items.remove(item)
                            print(f'You pick up the {item}.')
                    if(item_found==False):
                        print(f'There is no {item_to_get} anywhere.')
                else:
                    print(f'There is no {item_to_get} anywhere.')

            if(verb=="inventory"):
                
                if(len(user_inventory)==0):
                    print("You're not carrying anything.")
                else:
                    print("Inventory:")
                    for item in user_inventory:
                        print(f' {item}')

            if(verb=="quit"):
                print("Goodbye!")
                break

            if(verb=="drop"):
                if(len(command)<2):
                    print(f'Sorry,What do you need to {verb}?')
                    continue
                if('items' in map_object):
                    item_to_drop=command[1]
                    items=map_object['items']
                    for item in user_inventory:
                        if(item==item_to_drop):
                            item_found=True
                            items.append(item)
                            user_inventory.remove(item)
                            print(f'You drop  the {item}.')
                    if(item_found==False):
                        print(f'There is no {item_to_drop} to drop anywhere.')
                else:   
                    # print(f'There is no {item_to_drop} to drop anywhere.')
                    item_to_drop=command[1]
                    map_object['items']=[]
                    for item in user_inventory:
                        if(item==item_to_drop):
                            item_found=True
                            items.append(item)
                            user_inventory.remove(item)
                            print(f'You drop  the {item}.')
                    if(item_found==False):
                        print(f'There is no {item_to_drop} to drop anywhere.')

#  print(type(map_object.exits))
# json_str=json.loads(data[i])
# print(type(json_str))

# map=mapDecoder(data);

# print(map.name)
# play()
read(0)
process()