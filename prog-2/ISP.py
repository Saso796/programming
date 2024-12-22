from abc import ABC , abstractmethod

class phone(ABC):
    @abstractmethod
    def voice(self):
        pass
    
class text(ABC):
    @abstractmethod
    def text_message(self):
        pass
    
class camera(ABC):
    @abstractmethod
    def photo(self):
        pass
    
class mobile(phone , text ,camera):
    def voice():
        return 'I can talk' 
    def text_message():
        return 'I can message'
    def photo():
        return 'I can talk photos'
    
class oldmobile(phone , text ):
    def voice():
        return 'I can talk' 
    def text_message():
        return 'I can message'
    
print(mobile.voice()) 
print(oldmobile.text_message())   