from pyfiglet import Figlet
import qrcode


# print the store's name using pyglet
font = Figlet(font='standard')
print(font.renderText('Ehsan Store'))

# creates the products list. each item is a dictionary.
PRODUCTS_LIST = []

# load the data from file
def load(address):
  # it returns an object
  database = open(address, 'r+')
  # returns the whole text as a string with \n
  data = database.read()
  # creates a list of lines
  products = data.strip().split('\n')
  # creates a dictionary from each line
  for item in products:
    info = item.split(',')
    item_dict = {'barcode':info[0], 'name':info[1], 'price':int(info[2]), 'count':int(info[3])}
    PRODUCTS_LIST.append(item_dict)
  print('Loading the database... Done.')
  database.close()


# show menu
def menu():
  print('''
1. add new item to the store
2. edit product's info
3. search by name
4. qrcode
5. remove item
6. buy from the store
7. save and exit''')
  return int(input('\t> '))


# add new item
def add_item():
  while True:
    new_barcode = input('enter the barcode: ')
    # checks if this barcode already exists in the producsts list, if not creates a dict and add it to the end of the list
    if search(new_barcode) is False:
      new_item = {'barcode':new_barcode, 'name':input('enter the name: '), 'price':int(input('enter the price: ')), 'count':int(input('enter the count: '))}
      PRODUCTS_LIST.append(new_item)
      break
    else: print('already exists, enter another value')


# edit product's info
def edit():
  barcode = input('enter the name or the barcode of the item you want to edit: ')
  index = search(barcode)
  if index:
    PRODUCTS_LIST[index]['barcode'] = input('enter the new barcode: ')
    PRODUCTS_LIST[index]['name'] = input('enter the new name: ').title()
    PRODUCTS_LIST[index]['price'] = int(input('enter the new price: '))
    PRODUCTS_LIST[index]['count'] = int(input('enter the new count: '))
  else: print('item does not exist!')


# search by name and barcode, returns the index of False if the item doesn't exist
def search(argument):
  for idx, item in enumerate(PRODUCTS_LIST):
    if item['name'] == argument or item['barcode'] == argument:
      print(f"barcode: {item['barcode']}\tname: {item['name']}\tprice: {item['price']}\tcount: {item['count']}".expandtabs(10))
      return idx
  return False


# input: product's code | output: info in qrcode
def Qrcode():
  barcode = input('enter the name or the barcode: ')
  index = search(barcode)
  if index:
    image = qrcode.make(PRODUCTS_LIST[index])
    image.save(PRODUCTS_LIST[index]['name'] + '.png')
    print('Done.')
  else: print('item not found!')


# remove item by barcode
def remove():
  barcode = input('enter the name or the barcode: ')
  index = search(barcode)
  if index:
    PRODUCTS_LIST.pop(index)
    print('item removed successfully.')
  else: print('item not found')


def show_list():
  for item in PRODUCTS_LIST:
    values = item.values()
    for value in values:
      print(f'{value}\t'.expandtabs(10), end=' ')
    print()


# buy from the store
def buy():
  # total price
  total = 0
  invoice = ''
  while True:
    # item's price * amount
    tprice = 0
    # input: barcode
    name = input('enter the name or the barcode: ').title()
    # if don't exist: print message | if exists input: count
    idx = search(name)
    if idx:
      # if count < 0: print message | if count > 0: proceed
      amount = int(input('enter the amount: '))
      if PRODUCTS_LIST[idx]['count'] - amount >= 0:
        # if incentory is enough, update the count
        PRODUCTS_LIST[idx]['count'] -= amount
        tprice = PRODUCTS_LIST[idx]['price'] * amount
        invoice += f"{PRODUCTS_LIST[idx]['name']} * {PRODUCTS_LIST[idx]['price']} = {tprice}\n"
        total += tprice
      else: print('not enough inventory!')
    else: print('item not found!')
    # countinue till user says when
    if input('do you wanna continue? yes/no: ') == 'no':
      print()
      break
  # show invoice
  invoice += f'-----------\nTotal Price: {total}'
  print(invoice)


# save info on file on exit (overwrite)
def save_n_exit():
  write = open(address, 'w')
  for item in PRODUCTS_LIST:
    line = item.values()
    string = ','.join(map(str, line))
    write.write(string + '\n')
  write.close()


# Driver program
# address of the database file
address = 'database.txt'

load(address)

while True:
  # input the user's choice from the menu and call the appropriate function
  choice = menu()
  match choice:
    case 1:
      add_item()
    case 2:
      show_list()
      edit()
    case 3:
      search(input('enter the name:').title())
    case 4:
      show_list()
      Qrcode()
    case 5:
      show_list()
      remove()
    case 6:
      show_list()
      buy()
    case 7:
      save_n_exit()
      break
