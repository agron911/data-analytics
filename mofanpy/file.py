def f(x,a=1,b=1,c=0):
    return a*x**2+b*x+c

# print(f(3,a=3))

class File:
    def __init__(self,name,create_time='0623'):
        self.name = name
        self.create_time = create_time
        self.__delete = False
        self._type = '.txt'

    def change_name(self,new_name):
        self.name= new_name
    
    def get_info(self):
        return self.name + " is created at " + self.create_time

    def delete(self):
        self.__force_del()

    def __force_del(self):
        self.__delete=True
        return True

    def _soft_del(self):
        self.__force_del()
        return True

class Video(File):
    def __init__(self,name,window_size=(1080,720)):
        super().__init__(name=name,create_time='today')
        self.window_size = window_size

class Text(File):
    def __init__(self,name, language="zh-cn"):
        super().__init__(name=name,create_time="today")
        self.language=language
    
    def get_more_info(self):
        return self.get_info() + ' , using language of '+ self.language




my_file = File('aaa')
# print(my_file.name)

my_file.change_name('bbb')
# print(my_file.name)

# print(my_file.get_info())

v = Video('my_video')
t = Text('my_text')

# print(v.window_size)
# print(t.create_time)
# print(v.get_info())
# print(t.get_more_info())


# print(my_file.__delete)  # 會報錯
# print(my_file.__force_del()) # 報錯
# print(my_file._type)
# print(my_file._soft_del())
