def main(email):
    email_length = len(email)
    if '@' in email:
        
        at_sym = email.index('@')
        dot_sym = email.index('.')

        username = email[0:at_sym]
        host = email[at_sym+1:dot_sym]
        extension = email[dot_sym:email_length]

        print(f'Username: {username}\nHost: {host}\nExtension: {extension}')
        print(f'Visit https://{host}{extension} for more information')
    else:
        print('This is not an email')
main(email=str(input('Email: ')))
