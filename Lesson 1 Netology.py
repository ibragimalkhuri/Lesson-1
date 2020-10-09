#!/usr/bin/env python
# coding: utf-8

# # Задание 1

# In[5]:


phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(phrase_1)>len(phrase_2):
    print('Фраза 1 длиннее фразы 2')
else:
    print('Фраза 2 длиннее фразы 1')


# # Задание 2

# In[6]:


year = 2019

if year%4 == 0:
    print (str(year) + ' Високосный год')
else:
    print (str(year) + ' Обычный год')
    
    


# # Задание 3

# In[7]:



# Введите день: 
day =21
# Введите месяц: 
month = 'Июль'


if month == 'Январь':
 x = 1
elif month == 'Февраль':
 x = 2
elif month == 'Март':
 x = 3
elif month == 'Апрель':
 x = 4
elif month == 'Май':
 x = 5    
elif month == 'Июнь':
 x = 6    
elif month == 'Июль':
 x = 7
elif month == 'Август':
 x = 8    
elif month == 'Сентябрь':
 x = 9    
elif month == 'Октябрь ':
 x = 10    
elif month == 'Ноябрь':
 x = 11      
elif month == 'Декабрь':
 x = 12      
else:
 print('Месяц введен некорретно')

#print (x)    
 
#print(str(x)+str(day))    

y = str(x) + str(day)
a = 'Ваш знак зодиака: '    



if int(y) >= 321 and int(y)<= 420:
 print(a + 'Овен')
elif int(y)>=421 and int(y)<=520:
 print(a + 'Телец')
elif int(y)>=521 and int(y)<=621:
 print(a + 'Близнецы')
elif int(y)>=622 and int(y)<=722:
 print(a + 'Рак')
elif int(y)>=723 and int(y)<=823:
 print(a + 'Лев')
elif int(y)>=824 and int(y)<=923:
 print(a + 'Дева')
elif int(y)>=924 and int(y)<=1023:
 print(a + 'Весы')
elif int(y)>=1024 and int(y)<=1122:
 print(a + 'Скорпион')
elif int(y)>=1123 and int(y)<=1221:
 print(a + 'Стрелец')
elif int(y)>=1222 and int(y)<=120:
 print(a + 'Козерог')
elif int(y)>=121 and int(y)<=218:
 print(a + 'Водолей')
elif int(y)>=219 and int(y)<=320:
 print(a + 'Рыбы')


# # Задание 4

# In[8]:


width = 10
length = 205
height = 5


if width <15 and length <15 and height <15:
    print('Коробка №1')
elif width <15 and length <15 and height <15: 
    print ('Коробка №2')
elif width <15 and length > 200 and height <15: 
    print ('Упаковка для лыж')
else:
    print ('Стандартная коробка №3')


# # Задание 5

# In[9]:



number = '123456'

a = number[0]
b = number[1]
c = number[2]
d = number[3]
e = number[4]
f = number[5]


if int(a)+int(b)+int(c)==int(d)+int(e)+int(f):
    print ('Счастливый билет')
else:
    print('Неасчастливый билет')

