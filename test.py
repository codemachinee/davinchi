from yoomoney import Authorize, Client
from paswords import *
from datetime import *

seconds = (datetime.now().time().hour * 3600 + datetime.now().time().minute * 60 + datetime.now().time().second)

if 64800 <= seconds <= 86400:
    print('yes')
else:
    print('No')