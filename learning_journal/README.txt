#  Vic's Learning Journal

Getting Started
---------------

- cd <directory containing this file>

- $VENV/bin/pip install -e .

- $VENV/bin/pserve development.ini

## URL to Heroku deployment
https://vic-learning-journal.herokuapp.com/

## Coverage output for step2
---------- coverage: platform darwin, python 2.7.12-final-0 ----------
Name                            |       Stmts   |Miss  |Cover  |Missing
:------------------------------:|:-------------:|:----:|:-----:|:-----:
learning_journal/__init__.py    |           8   |   0  |100%   |
learning_journal/routes.py      |           5   |   0  |100%   |
learning_journal/views.py       |           14  |   0  |100%   |
                                |               |      |       |
TOTAL                           |           27  |   0  |100%   |
24 passed in 1.11 seconds


---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                            |        Stmts  |Miss  |Cover   |Missing
-------------------------------:|:-------------:|:----:|:------:|:-----:
learning_journal/__init__.py    |            8  |    0 |  100%  |
learning_journal/routes.py      |            5  |    0 |  100%  |
learning_journal/views.py       |            14 |    0 |  100%  |
                                |               |      |        |
TOTAL                           |            27 |    0 |  100%  |
24 passed in 1.42 seconds

## Coverage output for step3
---------- coverage: platform darwin, python 2.7.12-final-0 ----------
Name                                       Stmts   Miss  Cover   Missing
------------------------------------------------------------------------
learning_journal/__init__.py                   9      0   100%
learning_journal/models/__init__.py           22      0   100%
learning_journal/models/meta.py                5      0   100%
learning_journal/models/myentry.py             8      0   100%
learning_journal/routes.py                     5      0   100%
learning_journal/scripts/__init__.py           0      0   100%
learning_journal/scripts/entries.py            1      0   100%
learning_journal/scripts/initializedb.py      30     18    40%   24-27, 31-51
learning_journal/views/__init__.py             0      0   100%
learning_journal/views/default.py             44     16    64%   24, 33, 35-38, 46-49, 51-56
learning_journal/views/notfound.py             4      2    50%   6-7
------------------------------------------------------------------------
TOTAL                                        128     36    72%

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                                       Stmts   Miss  Cover   Missing
------------------------------------------------------------------------
learning_journal/__init__.py                   9      0   100%
learning_journal/models/__init__.py           22      0   100%
learning_journal/models/meta.py                5      0   100%
learning_journal/models/myentry.py             8      0   100%
learning_journal/routes.py                     5      0   100%
learning_journal/scripts/__init__.py           0      0   100%
learning_journal/scripts/entries.py            1      0   100%
learning_journal/scripts/initializedb.py      30     18    40%   24-27, 31-51
learning_journal/views/__init__.py             0      0   100%
learning_journal/views/default.py             44     16    64%   24, 33, 35-38, 46-49, 51-56
learning_journal/views/notfound.py             4      2    50%   6-7
------------------------------------------------------------------------
TOTAL                                        128     36    72%
