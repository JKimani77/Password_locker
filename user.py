class User:
    '''
    class that generates instance of users
    '''
    persons_list = [] #empty persons list
    user_list = []
    def __init__(self, nameone,nametwo,password):
        
        self.nameone = nameone
        self.nametwo = nametwo
        self.password = password 

    def save_person(self):
        User.persons_list.append(self)

    @classmethod
    def find_person(cls,nameone,password):
        for person in cls.persons_list:
            if person.password == password:
                return person