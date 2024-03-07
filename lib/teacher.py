#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
        ]
    def teach(self):
        """Teacher method that randomly selects and displays one of their knowledge"""
           # Get the length of the list
        max_index = len(self.knowledge) - 1
            # Generate a random index from  0 to max_index (inclusive)
        random_index = random.randint(0, max_index)
        return self.knowledge[random_index]
        # print("{} knows: {}".format(self.full_name(), self.knowledge[random_index]))
