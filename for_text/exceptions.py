class User_input_single_or_multiple_exception(BaseException):
    def __init__(self,message):
        super().__init__(f"Invalid input: {message}")
