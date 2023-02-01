

class MedicalHistoryIssues:

    def __init__(self, medIssue, year):

        self.medIssue = medIssue
        self.date = year


    def getMedIssue(self):
        return self.medIssue

    def getDate(self):
        return self.date