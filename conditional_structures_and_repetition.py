# conditional and repetition structures in python

def withdraw(value):
    balance = 500
    if balance >= value:
        balance -= value
        print('value withdrawn successfully! your balance is ', balance)
    else:
        print('balance insufficient!')

withdraw(100)

total = 5
for tot in range(total):
    print(tot)

for number in range(5):
    print(number)

VOWELS = 'AEIOU'
name = input('what is your name: ')

for letter in name:
    if letter.upper() in VOWELS:
        print(letter)


while True:
    opcao = int(input(' [1] withdraw \n [2] extract \n [3] logout \n : '))
    if opcao == 1:
        print('drawing...')
    elif opcao == 2:
        print('showing extract...')
    else:
        print('thank you for using our banking system, see you later!')
        break