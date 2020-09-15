def validasi(email):
    a= email.split('.')
    b= email.split('@')
    if len(a[1])>=5:
        print('Email tidak valid!!!,format ekstensi salah')
    else:
        print('ekstensi valid')
    if '!' in (b[0]):
        print('Tidak valid username salah')
    elif '@' in (b[0]):
        print('Tidak valid username salah')
    elif '#' in (b[0]):
        print('Tidak valid username salah')
    elif '$' in (b[0]):
        print('Tidak valid username salah')
    elif '%' in (b[0]):
        print('Tidak valid username salah')
    elif '^' in (b[0]):
        print('Tidak valid username salah')
    elif '&' in (b[0]):
        print('Tidak valid username salah')
    elif '*' in (b[0]):
        print('Tidak valid username salah')
    elif '(' in (b[0]):
        print('Tidak valid username salah')
    elif ')' in (b[0]):
        print('Tidak valid username salah')
    elif ')' in (b[0]):
        print('Tidak valid username salah')
    elif '?' in (b[0]):
        print('Tidak valid username salah')
    elif '<' in (b[0]):
        print('Tidak valid username salah')
    elif '>' in (b[0]):
        print('Tidak valid username salah')
    elif ':' in (b[0]):
        print('Tidak valid username salah')
    elif '-' in (b[0]):
        print('Tidak valid username salah')
    elif '=' in (b[0]):
        print('Tidak valid username salah')
    elif '+' in (b[0]):
        print('Tidak valid username salah')
    else:
        print('username valid')
    if '!' in (b[1]):
        print('Tidak valid hosting salah')
    elif '@' in (b[1]):
        print('Tidak valid hosting salah')
    elif '#' in (b[1]):
        print('Tidak valid hosting salah')
    elif '$' in (b[1]):
        print('Tidak valid hosting salah')
    elif '%' in (b[1]):
        print('Tidak valid hosting salah')
    elif '^' in (b[1]):
        print('Tidak valid hosting salah')
    elif '&' in (b[1]):
        print('Tidak valid hosting salah')
    elif '*' in (b[1]):
        print('Tidak valid hosting salah')
    elif '(' in (b[1]):
        print('Tidak valid hosting salah')
    elif ')' in (b[1]):
        print('Tidak valid hosting salah')
    elif '-' in (b[1]):
        print('Tidak valid hosting salah')
    elif '+' in (b[1]):
        print('Tidak valid hosting salah')
    elif '=' in (b[1]):
        print('Tidak valid hosting salah')
    elif '[' in (b[1]):
        print('Tidak valid hosting salah')
    elif '?' in (b[1]):
        print('Tidak valid hosting salah')
    elif '/' in (b[1]):
        print('Tidak valid hosting salah')
    else:
        print("Hosting Valid")
    
validasi('andre$%^&@gmail.com')
validasi('John85_cap@yah$%.com')
validasi('tony_stark@avengers.wakanda')
z=input("masukan email: ")
validasi(z)