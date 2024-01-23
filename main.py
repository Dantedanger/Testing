import uuid
from dataclasses import dataclass
from typing import List
from datetime import datetime
#
class User:
    def __init__(self, user_id:str,name:str,email:str,password:str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.curses: List[Curse] = []
        self.madecurses: List[Curse] = []
        self.favouriteCurses: List[Curse] = []
        self.doneCurses: List[Curse] = []
    
    def __eq__(self, other):
        if isinstance(other, User):
            return (self.user_id == other.user_id)
        else:
            return False
        
    def create_curse(self, name:str, sertificate:str, cost:str, subject:str):
        curse_id = str(uuid.uuid4())
        curse = Curse(curse_id, name, sertificate, cost, subject)
        self.madecurses.append(curse)
        return curse

    def save_curse(self, name:str, sertificate:str, cost:str, subject:str):
        curse_id = str(uuid.uuid4())
        curse = Curse(curse_id, name, sertificate, cost, subject)
        self.favouriteCurses.append(curse)
        return curse
        
   
def create_user(name:str,email:str,password:str):
    user_id = str(uuid.uuid4())
    user = User(user_id,name,email,password)
    return user
    
def login_user(user:User,name:str,email:str,password:str):
    if (email == user.email and password == user.password):
        return user
    return False

class Curse:
    def __init__(self, curse_id:str, name:str, sertificate:str, cost:str, subject:str):
        self.curse_id = curse_id
        self.name = name
        self.sertificate = sertificate
        self.cost = cost
        self.subject = subject
        self.lessons: List[Lesson] = []
        self.reviews: List[Review] = []

    def __eq__(self, other):
        if isinstance(other, Curse):
            return (self.curse_id == other.curse_id)
        else:
            return False
    
    def create_lesson(self, name:str):
        lesson_id = str(uuid.uuid4())
        lesson = Lesson(lesson_id, name)
        self.lessons.append(lesson)
        return lesson
    
    def search_curse(self, name:str, subject:str):
        if (name == self.name or subject == self.subject):
            return self.name
        
    def pass_curse(self, user:User):
        user.curses.append(self)
        return (self.lessons)

    def get_sertificate(self, user:User):
        if (self in user.doneCurses):
            return self.sertificate
        
    def get_olympia(self, user:User):
        self.pass_curse(self, user)
    
class Lesson:
    def __init__(self, lesson_id:str, name:str):
        self.lesson_id = lesson_id
        self.name = name
        self.elements: List[Element] = []
        self.forum: List[Forum] = []

    def __eq__(self, other):
        if isinstance(other, Lesson):
            return (self.lesson_id == other.lesson_id)
        else:
            return False

    def pass_lesson(self, curse: Curse, user:User):
        if (self in curse.lessons and curse in user.curses):
            return (self.elements, self.forum)
        
class Forum:
    def __init__(self, lesson:Lesson):
        self.lesson = lesson
        self.comments: List[Comment] = []

    def create_comment(self, sender:User, content:str, comment_id:str, name:str):
        comment_id = str(uuid.uuid4())
        comment = Comment(comment_id, sender, self, content, name)
        self.comments.append(comment)

class Comment:  
    def __init__(self, sender:User, forum:Forum, content:str, comment_id:str, name:str):
        self.comment_id = comment_id
        self.name = name
        self.sender = sender
        self.content = content
        self.date = datetime.utcnow()
        self.forum = forum

class Review:  
    def __init__(self, sender:User, content:str, curse:Curse, review_id:str, name:str):
        self.review_id = review_id
        self.sender = sender
        self.content = content
        self.curse = curse
        self.date = datetime.utcnow()

class Element:
    def __init__(self, id_element:str, type:str, contentelement:str):
        self.id_element = id_element
        self.type = type
        self.contentelement = contentelement