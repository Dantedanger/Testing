import unittest
import uuid
from main import User, Curse, Lesson, create_user, login_user

class TestUser(unittest.TestCase):

    def setUp(self):
        user_id = str(uuid.uuid4())
        self.user = User(user_id,'Kirill Ivanovich','ayhtyhty@mail.com','12w2wesf')

    def test_create_user(self):
        self.assertEqual(login_user(self.user, 'Ivan Ivanovich','adw@mail.com','12w2w'), False, 'correct user')
        created_user = create_user('Ivan Ivanovich','adw@mail.com','12w2w')
        self.assertIsNotNone(created_user,'correct created user')
    
    def test_login_user(self):
        log_user = login_user(self.user, 'Kirill Ivanovich','ayhtyhty@mail.com','12w2wesf')
        self.assertEqual(log_user, self.user,'correct login user')

    def test_create_curse(self):
        created_curse = self.user.create_curse('Math+', True, None, 'Math')
        self.assertIsNotNone(created_curse,'correct created curse')

    def test_save_curse(self):
        saved_curse = self.user.save_curse('Math', True, None, 'Math')
        self.assertEqual(self.user.favouriteCurses[0], saved_curse,'correct saved curse')

class TestCurseAndLessons(unittest.TestCase):

    def setUp(self):
        user_id = str(uuid.uuid4())
        self.user = User(user_id,'Kirill Ivanovich','ayhtyhty@mail.com','12w2wesf')

        curse_id = str(uuid.uuid4())
        self.curse = Curse(curse_id, 'Math', True, None, 'Math')
        
        self.user.doneCurses.append(self.curse)
        self.user.curses.append(self.curse)

        lesson_id = str(uuid.uuid4())
        self.lesson = Lesson(lesson_id, 'Introduction')
        self.user.curses[0].lessons.append(self.lesson)

    def test_create_lesson(self):
        created_lesson = self.curse.create_lesson("LessonNumber1")
        self.assertIsNotNone(created_lesson,'correct created lesson')
    
    def test_search_curse(self):
        search = self.curse.search_curse('Math', 'Math')
        self.assertEqual(search, self.curse.name,'correct search curse')
        
    def test_pass_curse(self):
        self.curse.pass_curse(self.user)
        self.assertEqual(self.user.curses[0], self.curse,'correct pass lesson')

    def test_get_sertificate(self):
        sertificate = self.curse.get_sertificate(self.user)
        self.assertEqual(self.user.doneCurses[0], self.curse,'correct find sertificate')
        self.assertIsNotNone(sertificate,'correct get sertificate')
        
    def test_get_olympia(self):
        self.curse.pass_curse(self.user)
        self.assertEqual(self.user.curses[0], self.curse,'correct get olympia')
    
    def test_pass_lesson(self):
        self.lesson.pass_lesson(self.curse, self.user)
        self.assertEqual(self.user.curses[0].lessons[0], self.lesson,'correct pass lesson')


if __name__ == '__main__':
    unittest.main()