from random import randint
passwd_length = randint(1, 100)

def random_passwd(n):
    passwd = ''
    for i in range(n):
        passwd += chr(randint(33, 126))
        
    return passwd
    
print(random_passwd(passwd_length))