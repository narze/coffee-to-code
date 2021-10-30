Human = object

class Me(Human):
    def drink(self, a_drink):
        if a_drink == 'Coffee':
            print('Code')

if __name__ == '__main__':
    me = Me()
    me.drink('Coffee')
