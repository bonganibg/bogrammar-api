from src.services.data_handling import DatabaseService
from src.models.reviewer import ReviewBacklogDTO

class Reviewer(DatabaseService):
    def __init__(self, db_name: str = "bogrammar.db") -> None:
        super().__init__(db_name)

    def update_review_score(self, review_id: int, score: int):
        """
            Changes the students score on a review

            Parameters:
                review_id (int): The ID for the review
                score (int): The updated score for the task
        """

        # Change the score in the Student_Task table
        update_query = f"""
            UPDATE Student_Task
            SET GRADE = {score},
            REVIEW_SUBMITTED = 0
            WHERE  STUDENT_ID = (SELECT STUDENT_ID FROM Task_Review WHERE REVIEW_ID = {review_id})
            AND TASK_ID = (SELECT TASK_ID FROM Task_Review WHERE REVIEW_ID = {review_id})
        """
        
        # Delete the record from the Task_Review table
        query = f"""
            DELETE 
            FROM Task_Review
            WHERE REVIEW_ID = {review_id}
        """

        self.run_query(update_query)
        self.run_query(query)
        
    def get_review_backlog(self):
        """
            Complie the fields to make a review object

            Return:
                a dictionary for the backlog
        """

        # Get the values that make up the backlog object from the Task_Review, Student, Task and Course tables
        query = f"""
            SELECT R.REVIEW_ID, S.FULL_NAME, S.STUDENT_NUMBER, S.FOLDER_LINK,
                   C.COURSE_NAME, T.NAME, T.FOLDER_LINK
            FROM Task_Review R, Student S, TASK T, Course C
            WHERE R.STUDENT_ID = S.STUDENT_ID
            AND R.TASK_ID = T.TASK_ID 
            AND C.COURSE_ID = S.COURSE_ID
        """

        keys = ["ReviewID", "StudentName", "StudentNumber", "FolderLink", 
                "Course", "Task", "TaskFolderLink"]
        
        data = self.run_query(query)

        review_backlog = self.convert_tuple_to_dict(keys, data)
        review_backlog_model = [ReviewBacklogDTO.parse_obj(review) for review in review_backlog]
        return review_backlog_model

    def convert_tuple_to_dict(self, keys: list, data: list) -> dict:
        """
            Joins a list of keys and list of tuples to make a dictonary

            Parameters:
                keys (list[str]): A list of keys 
                data (list[tuple]): a list of tuples containing data records

            returns:
                a dictionary list of all of the records
        """
        
        backlog = []

        for line in data:
            line = str(line)
            line = line.strip('(').strip(')')            
            line = line.split(',')

            backlog_dict = {}
            for key, value in zip(keys, line):
                value =value.strip().strip('\'')
                backlog_dict[key] = value
            
            backlog.append(backlog_dict)

        return backlog