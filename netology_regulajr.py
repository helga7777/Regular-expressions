from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import re
import csv
with open('phonebook_raw.csv',encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=',')
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# формируем корректный список
fio = ''
contacts_list_new = []
for id in contacts_list:
  f = []
  info = ''
  fio = str(id[0])+' ' + str(id[1]) +' '+ str(id[2])
  f = fio.split(' ')
  for i in range(3,len(id)):
    if len(id[i])>0:
      f.append(id[i])
    else:
      f.append(' ')
  contacts_list_new.append(f)

# убираем лишние пробелы
contacts_list_new_sort = []
for id in contacts_list_new:
  info = []
  for i in range(len(id)):
    f = ''
    f = f + id[i]
    if len(f) != 0:
      info.append(f)
  contacts_list_new_sort.append(info)
# print(contacts_list_new_sort)


# находим номера телефонов
for id in contacts_list_new_sort:
  for i in range(len(id)):
    text = id[i]
    pattern = r'(\+7|8)\s?\(?(\d{3})\)?(-|\s)?(\d{3})(-|\s)?(\d{2})(-|\s)?(\d{2})'
    result = re.sub(pattern,r'+7(\2)\4-\6-\8',text)
    id[i] = result
    if 'доб.' in text:
      pattern1 = r'\(?доб.\s?(\d*)\)?'
      result1 = re.sub(pattern1,r'доб.\1',result)
      id[i] = result1
# print(contacts_list_new_sort)

# объединяем дубликаты
count = 1
for id in contacts_list_new_sort:
  text = id[0]
  # print(id)
  for j in range(count,len(contacts_list_new_sort)):
      if text == contacts_list_new_sort[j][0]:
        index_fio = contacts_list_new_sort.index(id)
        contacts_list_new_sort[index_fio] = id + list(set(contacts_list_new_sort[j]) - set(id))
  count += 1
# print(contacts_list_new_sort)

# удаляем ненужный дубликат
count = 1
index_del = []
for id in contacts_list_new_sort:
  text = id[0]
  # print(id)
  end = len(contacts_list_new_sort)
  for j in range(count,end):
      if text == contacts_list_new_sort[j][0]:
        index_fio = contacts_list_new_sort.index(contacts_list_new_sort[j])
        index_del.append(index_fio)
  count += 1
print('Длина списка до удаления дубликатов', len(contacts_list_new_sort))
end = len(index_del)
for t in range(end-1,-1,-1):
  index = index_del[t]
  # print(index)
  # print((contacts_list_new_sort[4]))
  del(contacts_list_new_sort[index])
print('Длина списка после удаления дубликатов', len(contacts_list_new_sort))
print(contacts_list_new_sort)



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list_new_sort)