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

    @classmethod
    def find_by_acc_name(cls,account):
        for credential in cls.creds_list:
            if credential.account == account:
                return credential

    @classmethod
    def credential_exists(cls,account):
        for credential in cls.creds_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def reveal_credentials(cls):
        return cls.creds_list