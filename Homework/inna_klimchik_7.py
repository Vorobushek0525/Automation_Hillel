##########_Task_1_##########

print('(etnfづzxfk｡12dt◕`1ad‿6hns‿1zQY◕Cd$y｡FtSq)Ze6?づ#2)$'[0: 50: 5])

##########_Task_2_##########

days_and_hours = input("количество_земных_дней, количество_земных_часов: ").split(', ')
sol = (int(days_and_hours[0]) * 24 + int(days_and_hours[1])) / 24 / 1.02595675
print(f'количество_марсианских_солов: {sol}')

##########_Task_3_##########

text = input('Введите текст: ')
text = text.title()
text = ' ' + text + ' '
text = text.replace(' Черт ', ' #### ')
text = text.replace(' Черт ', ' #### ')
print(text)
