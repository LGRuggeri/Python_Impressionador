# 3. Faça um Programa que verefique o estado civil de uma pessoa. Se a letra digitada é 
# "C" (Casado), "S" (Solteiro), "D" (Divorciado), "V" (Viúvo) ou "O" (outros). 
# Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil.


est_civil= input('Digite o estado civil sendo "C- Casado", "S- Solteiro", "D- Divorciado", "V- Viuvo", "O- Outros": ')



if est_civil.upper()=='C':
    est_civil='CASADO'
    print(f'O seu status cívil é {est_civil}')    
elif est_civil.upper()=='S':
    est_civil='SOLTEIRO'
    print(f'O seu status cívil é {est_civil}')    
elif est_civil.upper()=='D':
    est_civil='DIVORCIADO'
    print(f'O seu status cívil é {est_civil}')    
elif est_civil.upper()=='V':
    est_civil='VIUVO'
    print(f'O seu status cívil é {est_civil}')   
elif est_civil.upper()=='O':
    est_civil='OUTROS'
    print(f'O seu status cívil é {est_civil}')
    
    
    