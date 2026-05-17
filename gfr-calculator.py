print ('GFR Calculator (CKD-EPI 2021)')


sex = str (input ('Sex (m/f):'))
sex = sex.lower()

if sex not in ['m', 'f']:
    print('Invalid sex input')
    exit()


try:
    age = float(input('Enter age: '))
    k_ru = float(input('Serum creatinine (µmol/L): '))
    
except ValueError:
    print('Invalid input')
    exit()



# Перевод мкмоль/л в мг/дл:

'''
1 мкмоль/л = мг/дл * 88.4

1 мг/дл = 1 мкмоль/л : 88.4

eng = ru : 88.4
'''

k_eng = k_ru/88.4

    

gfr_m = 142 * (min(k_eng/0.9, 1)**(-0.302)) * \
      (max(k_eng/0.9, 1)**(-1.200)) * \
      (0.9938 ** age)

gfr_f = 142 * (min(k_eng/0.7, 1)**(-0.241)) * \
      (max(k_eng/0.7, 1)**(-1.200)) * \
      (0.9938 ** age) * 1.012


gfr = None

if sex == 'f':
    print('Sex F')
    gfr = gfr_f

elif sex == 'm':
    print('Sex M')
    gfr = gfr_m
    
else:
    print('Sex ?')



print(f'GFR: {gfr:.1f} mL/min/1.73m²')

    
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
