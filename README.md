# Instructions
For this homework assignment, you will parse through a set of 10,000 emails for the purpose of pre- analysis processing. These emails are a sample from a collection of around 500,000 emails known as the “Enron Email Dataset”. This dataset contains emails sent by employees of Enron after the collapse of the company. The entire dataset can be found here: Kaggle Enron Dataset

In order to parse an email, you must first be familiar with the structure of emails. When we send emails we are not only sending heading and body content information, we are also sending metadata that describes the email structure in detail. This is known as the “header” and will contain data relating to the sender, receivers, CC information, routing information, etc. This header is formatted enough that we can use regular expressions in order to identify the information that we are interested in.


# Instructions
- Your script should be named enron.py.
- Your script should contain two classes, Server and Email. At the end of the script should be an if **__name__ == "__main__":** statement. Specifications for each of these required program elements are given below. You may write additional classes, methods, and/or functions if you wish.
- The name of your files should consist exclusively of lower-case letters, numbers, and underscores, and the file extension .py. Your filename should not start with a number.
- Your script MUST contain docstrings.
- You should place the text file in the same directory as your python script.

# Server class

**Functionality**
- This function takes a string and returns a string containing only the lower cased alphabetical characters. If the item being passed in is not a string a TypeError should be raised.

**Parameters**
- word: the input string that contains a word. This word may contain non-alphabetical characters such as numbers or punctuation marks.

**Returns**
- A lowercase string containing only the lowercased alphabetical characters from the input string with all of the non alphabetical characters stripped away. If the string did not contain any alphabetical characters (the string is empty), the function will return None.


# Email class
# main()
# parse_args()
# if __name__ == "__main__":
# Running your program
