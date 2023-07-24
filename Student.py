listStudent = []

class Student (object):
    def __init__(self, _indentification, _name, _lastName, _ege, _note1, _note2, _note3):
        self.iindentification = _indentification
        self.name = _name
        self.lastName = _lastName
        self.age = _ege
        self.note1 = _note1
        self.note2 = _note2
        self.note2 = _note3
        
        self.final_note = (_note1 + _note2 + _note3) / 3
        self.history =  []
        
    def Develiver_data(self):
        print("No. indentification: {} - {}  {} - final  note".format(self.iindentification, self.name, self.lastName, self.final_note))
    
    def edit_notes (self, _note1, _note2, _note3):
        self.note1 = _note1
        self.note2 = _note2
        self.note3 = _note3
        
        self.final_note = (_note1 + _note2 + _note3) / 3
        print("¡Successful registration!")  
        
    def incluide_events (self, _note1, _note2, _note3):
        return("Modification: note_1: {}  note_2:{}  note_3: {}".format(_note1, _note2, _note3))
    
    def Develiver_history(self):
        print("No. indentification: {} - {} {}".format(self.iindentification, self.name, self.lastName, ))     