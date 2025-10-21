import random
import string

#This is where further support methods may go
#If not used, consider adding methods such as generate string, click random element, take screenshot etc.

class ExecutionHooks:
    def generate_random_string(self, length):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return random_string
