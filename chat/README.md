This a demo project for Django channels.

See https://channels.readthedocs.io/en/stable/tutorial/index.html

Note
---------
- 'asgiref==3.4.x' causes get_running_loop error for runworker, see https://github.com/django/asgiref/issues/278.
  This can be fixed by downgrading to 'asgiref==3.3.4'