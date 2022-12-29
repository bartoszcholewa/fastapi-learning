from datetime import datetime
from enum import Enum
from typing import List, Optional


class Major(str, Enum):
    CS = 'Computer Science'
    IT = 'Information Technology'
    Math = 'Mathematics'
    Chem = 'Chemistry'
    Agri = 'Agriculture'
    AgChem = 'Agricultural Chemistry'
    Phy = 'Physics'
    Stat = 'Statistics'
    CommArts = 'Communication Arts'
    FArts = 'Fine Arts'
    Archi = 'Architecture'
    Kinetics = 'Human Kinetics'
    Physio = 'Physiology'
    Psych = 'Psychology'
    Hist = 'History'
    Archeo = 'Archeology'
    ChemEng = 'Chemical Engineering'
    EEng = 'Electrical Engineering'
    BioChem = 'BioChemistry'
    MathEduc = 'Math Education'


class Assignment:
    def __init__(self, assgn_id: int, title: str, date_due: datetime, course: str):
        self.assgn_id: int = assgn_id
        self.title: str = title
        self.date_completed: Optional[datetime] = None
        self.date_due: datetime = date_due
        self.rating: float = 0.0
        self.course: str = course

    def __repr__(self):
        return ' '.join([
            str(self.assgn_id),
            self.title,
            self.date_completed.strftime("%d/%m/%Y, %H:%M:%S"),
            self.date_due.strftime("%d/%m/%Y, %H:%M:%S"),
            str(self.rating)
        ])

    def __str__(self):
        return ' '.join([
            str(self.assgn_id),
            self.title,
            self.date_completed.strftime("%d/%m/%Y, %H:%M:%S"),
            self.date_due.strftime("%d/%m/%Y, %H:%M:%S"),
            str(self.rating)
        ])


class StudentBin:
    def __init__(self, bin_id: int, stud_id: int, faculty_id: int):
        self.bin_id: int = bin_id
        self.stud_id: int = stud_id
        self.faculty_id: int = faculty_id
        self.assignment: List[Assignment] = list()

    def __repr__(self):
        return ' '.join([
            str(self.bin_id),
            str(self.stud_id),
            str(self.faculty_id)
        ])

    def __str__(self):
        return ' '.join([
            str(self.bin_id),
            str(self.stud_id),
            str(self.faculty_id)
        ])
