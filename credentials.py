class Creds:
    '''
    class that generates new instances of credentials

    '''
    creds_list = [] #empty credentials list
    def __init__(self,account,password):

        self.account = account
        self.password = password

    def save_creds(self):
        Creds.creds_list.append(self)

    def rm_creds(self):
        Creds.creds_list.remove(self)