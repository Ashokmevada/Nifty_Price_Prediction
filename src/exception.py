import sys
from src.logger import logging

class CustomException(Exception):

    def __init__(self, error_message , error_detail:sys):
        super().__init__(err_message)
        self.error_message = error_message_detail(error_message , error_detail)

    def __str__(self):
        return self.error_message

        
