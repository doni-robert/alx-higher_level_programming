#!/usr/bin/python3
""" Defines a class Student """


class Student:
    """ A class representing a student """
    
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student

        Args:
            first_name(str): The student's first name
            last_name(str): The student's last name
            age(int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        my_dic = self.__dict__
        new_dic = {}
        if type(attrs) == list:
            if all(type(word) is str for word in attrs):
                for word in attrs:
                    if word in my_dic:
                        new_dic[word] = my_dic[word]
                return new_dic
        
        return my_dic
