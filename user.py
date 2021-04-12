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