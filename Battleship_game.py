#from numpy import *
from random import *
from pandas import *
import string
from IPython.core.display import display, HTML


flag = 0
loc_hist = []
keys = list('0123456789')
col_dic = {keys[i]:'○' for i in range(10)}
comp_dic = {keys[i]:'○' for i in range(10)}
battle_area = DataFrame(col_dic, index=list('ABCDEFGHIJK'), columns=list('0123456789'))
unseen1 = battle_area.copy()
attack_area = DataFrame(comp_dic, index=list('ABCDEFGHIJK'), columns=list('0123456789'))
unseen2 = attack_area.copy()# print(battle_area)
print('''       You can set the boat either vertical or horizontal
                     Your points should be like: a2 b2''')


def fill(lst, ground):
  globals()
  for i in lst:
    ground.at[i[0:1],i[1:]] = '■'    
    # print(battle_area)    
    return

def check(n,lst):
  flag = 0
  a = lst[0][:1]
  b = lst[0][1:]
  #print(a,b)
  if len(lst) != n:
    #print(flag)        
    return flag
  else:
    for i in range(1,n):
      if lst[i][:1] == a and ord(lst[i][1:]) - ord(lst[i-1][1:]) == 1:
        flag = 1            
      elif lst[i][1:] == b and ord(lst[i][:1]) - ord(lst[i-1][:1]) == 1:                
        flag =1            
      else:                
        flag = 0        
        #print(flag)        
        return flag

def const_num(n):    
  globals()    
  ch = choice(string.ascii_letters).upper()    
  num = str(randint(0, 10))    
  if ch <= 'K':        
    lst = [ch+num]        
    if ord('K') - ord(ch) >= n:            
      for i in range(1,n):                
        lst.append(chr(ord(ch) + i) + num)        
    else:            
      for i in range(1,n):                
        lst.append(chr(ord(ch) - i) + num)    
  else:        
    return const_num(n)    
  return lst

def const_alpha(n):    
  globals()    
  ch = choice(string.ascii_letters).upper()    
  num = str(randint(0, 10))    
  if ch <= 'K':        
    lst = [ch + num]        
    if 9 - int(num) >= n:            
      for i in range(1,n):                
        lst.append(ch + str(int(num)+1))        
      else:            
        for i in range(n):                
          lst.append(ch + str(int(num)-1))        
          return lst
    else:        
      return const_alpha(n)
ran = [const_alpha, const_num]
fill(choice(ran)(2),unseen1)# print(unseen1)

def display_side_by_side(dfs:list, captions:list):    
  """Display tables side by side to save vertical space    Input:        dfs: list of pandas.DataFrame        captions: list of table captions    """    
  output = ""    
  combined = dict(zip(captions, dfs))    
  for caption, df in combined.items():        
    output += df.style.set_table_attributes("style='display:inline'").set_caption(caption)._repr_html_()        
    output += "\xa0\xa0\xa0"    
    display(HTML(output))

display_side_by_side([battle_area,attack_area],['battle', 'attack'])
def boat_pos():    
  patrol_boat = input('Enter 2 consecutive points from the board with space in between: ').upper().split(' ')    
  if check(2,patrol_boat) == 0:        
    print('wrong input type, pls try again: ')        
    return boat_pos()    
  else:        
    fill(patrol_boat,battle_area)

def usr_attack():    
  point = input('At which point are you going to attack? ').upper()    
  # os.system('cls')    
  if len(point) == 2 and point[:1]<='K':        
    if attack_area.at[point[:1], point[1:]] == '▣' or attack_area.at[point[:1], point[1:]] == '◉':            
      print('Already attacked!!!')        
    elif unseen1.at[point[:1],point[1:]]=='■':            
      attack_area.at[point[:1], point[1:]] = '▣'            
      unseen1.at[point[:1], point[1:]] = '▣'            
      print('attack area : ', attack_area)        
    else:            
      attack_area.at[point[:1], point[1:]] = '◉'            
      print('attack area : ', attack_area)    
  else:        
    print(" Pls enter b/w A0 to K9")        
    return usr_attack()

def attack_gen():    
  globals()    
  a = choice(string.ascii_letters).upper()    
  b = str(randint(0,10))    
  if a <= 'K':        
    if battle_area.at[a, b] == '▣' or battle_area.at[a, b] == '◉':            
      return attack_gen()        
    elif battle_area.at[a,b]=='■':            
      battle_area.at[a,b] = '▣'            
      # loc_hist.append(a+b)            
      print('battle area : ', battle_area)            
      return battle_area
    else:            
      battle_area.at[a,b] = '◉'            
      print('battle area : ', battle_area)            
      return battle_area
  else:        
    attack_gen()

boat_pos()

def itt(j):    
  globals()    
  if unseen1[str(j)].str.contains('■').any():        
    usr_attack()        
    print('attack area: ', attack_gen())        
    return itt(j)    
  elif j <= 8:        
    return itt(j+1)    
  else:        
    if not unseen1[str(j)].str.contains('■').any():            
      print('Congratulations Captain!!! You won the war 🤗')            
      return attack_area
    else:            
      print('Sorry Captain, you have lost the war, try next time 😞!!')
      print(itt(0))
