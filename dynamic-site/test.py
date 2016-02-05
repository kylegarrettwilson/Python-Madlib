class Phone(object):  # super class
    def __init__(self): # initializing function
        self._phone_numba = ''   # super class attributes
        self._phone_id = ''  # super class attributes

class NewPhone(Phone):   # sub class
    def __init__(self):  # initializing function
        super(Phone, self).__init__()   # constructor for super class
        self._phone_numba = '541-987-0977'  # changing the attributes inhereted from the super class
        self._phone_id = 'Kyle Wilson'