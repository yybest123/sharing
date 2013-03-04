#coding:utf-8

from  handlers.home import HomeHandler
from  handlers.login import LoginHandler
from  handlers.validate import ValidateHandler
from  handlers.signup import SignupHandler
from handlers.group import GroupHandler
url_patterns = [
        (r"/", HomeHandler),
        (r"/login",LoginHandler),
        (r"/validate",ValidateHandler),
        (r"/signup",SignupHandler),
        (r"/group/([0-9]+)", GroupHandler),
        ]

