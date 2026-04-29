print ('GFR Calculator (CKD-EPI 2009)')


sex = str (input ('Sex (m/f):'))
race = str (input ('African American? (yes/no):'))
age = float (input ('Enter your age:'))

k_ru = float (input ('Serum creatinine (µmol/L)'))


# Перевод мкмоль/л в мг/дл:

'''
1 мкмоль/л = мг/дл * 88.4

1 мг/дл = 1 мкмоль/л : 88.4

eng = ru : 88.4
'''

k_eng = k_ru/88.4

'''
Отрицательная степень:

X**(-2) == 1/(x**2)
'''


# Различные формулы:

formula_1 = 144 * ((k_eng/0.7)**(-0.329)) * (0.993 ** age)

formula_2_4 = 144 * ((k_eng/0.7)**(-1.209)) * (0.993 ** age)

formula_3 = 144 * ((k_eng/0.7)**(-0.411)) * (0.993 ** age)


if sex == 'f':
    print('Sex F')
    
    if k_eng <= 0.7:
        formula = formula_1
    else:
        formula = formula_2_4

elif sex == 'm':
    print('Sex M')
    
    if k_eng <= 0.9:
        formula = formula_3
    else:
        formula = formula_2_4

else:
    print('Sex ?')
    
        
# Негроидная раса:

if race == 'yes':
    gfr = formula * 1.159
elif race == 'no':
    gfr = formula
else:
    print('African American?')
    

print (gfr)

    
if gfr > 90:
    print ('G1: Normal or high')
elif gfr < 15:
    print ('G5: Kidney failure')
elif gfr < 30 and gfr >= 15:
    print ('G4: Severely decreased')
elif gfr >=30 and gfr < 45:
    print ('G3b: Moderately to severely decreased')
elif gfr < 60 and gfr >= 45:
    print ('G3a: Mild to moderately decreased')
else:
    print ('G2: Mildly decreased')



# проверить правильность формулы и математического рассчета!

