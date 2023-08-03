# Django_TestProject1_LaurenSherburne
I just want to see if I can get learn how to use django on my own so...here goes! In this project, I am following along with the tutorial from
the django documentation: https://docs.djangoproject.com/en/4.2/intro/


***I keep forgetting that the cmd equivalent of "ls" is "dir"***

My Notes:
 - Run using the command 'python manage.py runserver' in cmd terminal (make sure you're in /Django_TestProject1/mysite otherwise you won't be able to access manage.py)
 - Admin page credentials: user=admin, password=123456
 - The 3 steps for making model changes:
    (1) Change your models (in models.py)
    (2) Run python manage.py makemigrations to create migrations for those changes
    (3) Run python manage.py migrate to apply those changes to the database

    DATABASE NOTES
     - Open database shell: python manage.py dbshell (.quit to close)
     - python shell for API: python manage.py shell (quit() to close)
     - SQLite database is the default configuration, included in Python
     - It is worth noting that if this project was expected to be anything other than a beginner learning django for the first time, using SQLite would not be wise. I would want to use something that is more scaleable for a real project. (https://docs.djangoproject.com/en/4.2/topics/install/#database-installation)




***************************************************************************************************
*** Part 2 Python shell querying the API ***
>>> from polls.models import Choice, Question
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>
>>> q = Question(question_text="How are you?", pub_date=timezone.now())
>>> Question.objects.all()
<QuerySet [<Question: What's up?>, <Question: How are you?>]>
>>> Question.objects.all()
<QuerySet [<Question: What's up?>, <Question: How are you?>]>
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\lkshe\AppData\Local\Programs\Python\Python311\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lkshe\AppData\Local\Programs\Python\Python311\Lib\site-packages\django\db\models\query.py", line 640, in get
    raise self.model.MultipleObjectsReturned(
polls.models.Question.MultipleObjectsReturned: get() returned more than one Question -- it returned 2!
>>> current_month = timezone.now().month
>>> Question.objects.get(pub_date__month=current_month) 
<Question: How are you?>
>>> Question.objects.get(id=2)
<Question: How are you?>
>>> Question.objects.get(id=3) 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\lkshe\AppData\Local\Programs\Python\Python311\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\lkshe\AppData\Local\Programs\Python\Python311\Lib\site-packages\django\db\models\query.py", line 637, in get
    raise self.model.DoesNotExist(
polls.models.Question.DoesNotExist: Question matching query does not exist.
>>> Question.objects.get(pk=1)
<Question: What's up?>
>>> q.was_published_recently()
True
>>> Question.objects.get(pk=1) 
<Question: What's up?>
>>> q.choice_set.all()
<QuerySet []>
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky!", votes=0) 
<Choice: The sky!>
>>> q.choice_set.create(choice_text="Just hacking again :)", votes=0) 
<Choice: Just hacking again :)>
>>> c = choice_set.create(choice_text="Just hacking again :)", votes=0)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'choice_set' is not defined
>>> c = q.choice_set.create(choice_text="Just hacking again :)", votes=0) 
>>> c.question
<Question: How are you?>
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'RelatedManager' object has no attribute 'delete'
>>> Choice.objects.filter(question__pub_date__year=current_year)0
  File "<console>", line 1
    Choice.objects.filter(question__pub_date__year=current_year)0
                                                                ^
SyntaxError: incomplete input
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much!>, <Choice: The sky...lol>, <Choice: Not much>, <Choice: The sky!>, <Choice: Just hacking again :)>, <Choice: Just hacking again :)>]>
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
(2, {'polls.Choice': 2})
***************************************************************************************************
