import os 

print(os.getcwd())
print(os.listdir())

if os.path.exists('./agron'):
    print('user exist')
else:
    os.makedirs('agron',exist_ok=True)
    print('user created')

if os.path.exists('agron'):
    os.removedirs('agron')
    print('rm user')
else:
    print("user doesn't exists")