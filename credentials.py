class Creds:
    '''
    class that generates new instances of credentials

    '''
    creds_list = [] #empty credentials list
    def __init__(self,account,password):

        self.account = account
        self.password = password
