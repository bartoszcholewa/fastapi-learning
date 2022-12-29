from uuid import uuid4

from faculty_mgt.models.data.faculty import Assignment
from faculty_mgt.repository.assignments import AssignmentSubmissionRepository


class AssignmentSubmissionService:
    def __init__(self):
        self.repo: AssignmentSubmissionRepository = AssignmentSubmissionRepository()

    def create_workbin(self, stud_id: int, faculty_id: int):
        bin_id = uuid4().int
        result = self.repo.create_bin(stud_id=stud_id, bin_id=bin_id, faculty_id=faculty_id)
        return result, bin_id

    def add_assignment(self, bin_id: int, assignment: Assignment):
        result = self.repo.insert_submission(bin_id=bin_id, assignment=assignment)
        return result

    def remove_assignment(self, bin_id: int, assignment: Assignment):
        result = self.repo.delete_submission(bin_id, assignment)
        return result

    def list_assignments(self, bin_id: int):
        return self.repo.get_submissions(bin_id)
