# load the data
def load():
  # i used try except for more error readablity 
  try:
    # it fills database with all the strings in .txt file
    database = open(address, 'r').read()
    # here we split data by newline
    data = database.strip().split('\n')
    # create a list of dictionaries from words
    for i in range(0, len(data), 2):
      info = {'english':data[i], 'persian':data[i + 1]}
      dictionary.append(info)
  # if file not found print the appropiate error and close the program
  except FileNotFoundError:
    print('database not found!')
    exit()


def menu():
  print('''
  1. english to persian trasnlator
  2. persian to english trasnlator
  3. add a new word
  4. save and exit''')
  return int(input('\t> '))


# add new words
def add():
  english = input('enter your word in English: ')
  # checks if already exists
  if search(english) == False:
    persian = input('enter your word in Persian: ')
    # it'll create a dictionary and add the word to the database
    info = {'english':english, 'persian':persian}
    dictionary.append(info)
    print('Done.')
  else: print('your word already exists!')

# search
def search(argument):
  for item in dictionary:
    if item['english'] == argument or item['persian'] == argument:
      return item
  return False


# translates engilsh to persian
def english_to_persian():
  # input all the sentences
  sentence = input('enter your sentence in english: ').strip().split('.')
  translation = ''
  # split the sentence by line
  for item in sentence:
    # split each line by word
    line = item.split()
    for word in line:
      # if a translation exists add it to the result
      if search(word):
        info = search(word)
        translation += info['persian'] + ' '
      # if not, put the word itself
      else: translation += word + ' '
    translation += '\n'
  return translation

  
# translates persian to english
# same as previuos function
def persion_to_engilsh():
  sentence = input('enter your sentence in persian: ').strip().split('.')
  translation = ''
  for item in sentence:
    line = item.split()
    for word in line:
      if search(word):
        info = search(word)
        translation += info['english'] + ' '
      else: translation += word + ' '
    translation += '\n'
  return translation

# saves the changes on the file
def save_n_exit():
  writing = open(address, 'w')
  for item in dictionary:
    line = list(item.values())
    # string = ''.join(line)
    writing.write(f'{line[0]}\n{line[1]}\n')
  writing.close()


dictionary = []
address = 'Pylearn/Session 7/translate.txt'
load()
while True:
  # input the user's choice from the menu and call the appropriate function
  choice = menu()
  match choice:
    case 1:
      print(english_to_persian())
    case 2:
      print(persion_to_engilsh())
    case 3:
      add()
    case 4:
      save_n_exit()
      break