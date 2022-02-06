data = input('Привет! \nВведите Ваше имя, пол, возраст (например: Инна, Ж, 27): ')
name = data.split(', ')[0].lower()
gender = data.split(', ')[1]
age = int(data.split(', ')[2])
answer1 = 0 # "StarWars" или "Мандалорец" for М and between 10 - 14 and over 30
answer2 = 0 # "TMNT" for М and less than 12
answer3 = 0 # "Трансформеры" for Ж and between 22 - 32
answer4 = 0 # "Инсургент" for Ж and less than 16
answer5 = 0 # "Дурак" for name Женя

# Name check:
if 'admin' in name:
    print("Привет, повелитель!")
if name == 'женя':
    answer5 += 4
if name == 'guido':
    print("Огромное спасибо!")

# Gender check:
if "М" in gender:
    answer1 += 3
    answer2 += 3
else:
    answer3 += 3
    answer4 += 3

# Age check:
if 10 < age < 14:
    answer1 += 2
if age < 12:
    answer2 += 2
if age > 30:
    answer1 += 2
if 22 < age < 32:
    answer3 += 2
if age < 16:
    answer4 += 2


answers_list_name = ('"StarWars" или "Мандалорец"', '"TMNT"', '"Трансформеры"', '"Инсургент"', '"Дурак"')
answers_list_value = (answer1, answer2, answer3, answer4, answer5)

print("Советую Вам посмотреть " + answers_list_name[answers_list_value.index(max(answers_list_value))])