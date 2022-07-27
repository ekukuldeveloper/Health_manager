read_or_write = int(input('Welcome type 1 to Log Data or 2 to retrieve Data:'))
claint_data = {'Harry':{1:'HarryExcersise.txt',2:'HarryFood.txt'},
               'Rohan':{1:'RohanExcersise.txt',2:'RohanFood.txt'},
               'Hammam':{1:'HammamExcersise.txt',2:'HammamFood.txt'}}
def getdate():
    import datetime
    return datetime.datetime.now()
time = getdate()
# print(_time)
user_input= claint_data[input('Eenter the claint name:')][int(input('For Excersise type 1 and for Food type 2:'))]

if read_or_write==1:
    def file_writing(a,b):
        with open(a,'a') as f:
         f.write(str(b)+"\t")
         f.write(input('Enter Data\n')+'\n')

        print('You sucssesfully entered the data')
    file_writing(user_input,time)
else:
    def file_reading(b):
        with open(b) as u:
            user_data=u.read()
            print(user_data)
    file_reading(user_input)
