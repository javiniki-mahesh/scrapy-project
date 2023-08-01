from exceptions import User_input_single_or_multiple_exception

class User_interest:

    def get_absolute_or_relative(self):
        input_abs_rel = input("Enter abs if you want extract absolute data\n \
                Enter rel if you want to extract relative data : ")
        return input_abs_rel
    
    def single_or_multiple(self):
        try:
            user_interest_of_single_or_multiple = int(input('Enter 1 if you want to extract the data from single page\n Enter 2 if you want to extract the data from multiple pages: '))
        except ValueError:
            print("Enter only either 1 or 2")
            return self.single_or_multiple()
        else:
            return user_interest_of_single_or_multiple
        
    def what_on_multiple_data(self):
        try:
            user_interest_on_multiple_data = int(input('Enter 1 to get element wise items (prefered): \n Enter 2 to get indivisible tag items data (html tags): \n Enter 3 to get all data in single items structure (consolidated): \n If you want to travel through each link and extract the text data enter 4 : \n Your option: '))
        except ValueError:
            print('Enter only values listed ')
            return self.what_on_multiple_data()
        else:
            return user_interest_on_multiple_data
        
    
