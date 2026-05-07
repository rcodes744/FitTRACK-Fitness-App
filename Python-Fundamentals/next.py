print('Welcome to Eligibility Checker!')
for i in range(1,11):
    age = int(input(f'Enter the age : '))
    Marks=float(input(f'Enter the marks obtained'))
    state=input(f'Enter the state (GJ for Gujarat,DL for Delhi, O for Others): ')
    if age <=20 and Marks>=60 : 
        print('You are eligible to apply!')
    elif age<=20 and Marks>=50 and state=='GJ':
        print('You are eligible to apply!')
    elif age<=22 and Marks>=60 and state=='DL':
        print('You are eligible to apply!')
    else:
        print('You are not eligible to apply!')
    choice=input('Do you want to check another eligibility (Y/N)? ')
    if choice.upper() != 'Y':
        break
print('Thank you for using Eligibility Checker!')


