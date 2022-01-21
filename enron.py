
from argparse import ArgumentParser
import re
import sys

class Server():
    """
    This class stores the data for all emails found in the dataset

    Attributes:
        emails - a list of Email objects where each object corresponds to one email
    """
    def __init__(self, path):
        with open(path, 'r', encoding="utf-8") as f:
            file = f.read()
            raw_file = file.split("End Email")
            raw_file = raw_file[:-1]
        self.emails = []
        for email in raw_file: 
            message_id = re.search(r'Message-ID: <.+>', email)
            if message_id is None:
                message_id = ('')
            else: 
                message_id = message_id.groups()

            date = re.search(r"(?<=Date:) (.+)", email)
            if date is None:
                date = ('')
            else: 
                date = date.groups()
        
            subject = re.search(r"subject: (.*)", email)
            if subject is None:
                subject = ('')
            else: 
                subject = subject.groups()

            #Works 
            sender = re.search(r"From: (.*)", email)
            if sender is None:
                sender = ('')
            else: 
                sender = sender.groups()

            #Works 
            receiver = re.search(r"To: (.*)", email)
            if receiver is None:
                receiver = ('')
            else: 
                receiver = receiver.groups()


            body = re.search(r'^\n(.+\n)+\n+', email)
            if body is None:
                body = ('')
            else: 
                body = body.groups()
            
            self.emails.append(Email(message_id, date, subject, sender, receiver, body))
                


class Email():
    """
    This class stores the data related to individual email messages

    Attributes:
        message_id(str): The message id unique to each email message

        date(str): The date associated with each email message, does not need to be formatted, 
        but should contain only date/time 

        subject(str): The subject of each email message 

        sender(str): The sender of each email message
        
        receiver(str): The receiver of each email message

        body(str): The body message of each email message
    """
    def __init__(self,message_id, date, subject, sender, receiver, body):
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body

def main(path):
    """
    Creates an instance of Server class using the Path that
    was passed in and save that to a variable

    Args:
        path: a string that represents the path of the text
        file that will be parsed

    Returns:
        integer: the length of the emails attribute of that instance
    """    
    server_class = Server(path)
    return len(server_class.emails)

def parse_args(args_list):
    """
    Creates an instance of the ArgumentParser class from the argparse module

    Use add_argument() method of ArgumentParser instance to add required agreement

    Args:
        args_list - a list of strings containing the command-line arguments
        for the program (pass sys.argv[1:] as argument when calling)

    Returns:
        The ArgumentParser object created
    """
    parser = ArgumentParser()
    parser.add_argument("path", type = str)
    return parser.parse_args(args_list)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.path)
