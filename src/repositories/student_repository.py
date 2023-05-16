from src.services.data_handling import DatabaseService
from src.models.student import StudentDashboardDTO


class Student(DatabaseService):    
    def __init__(self, db_name: str = "bogrammar.db") -> None:
        super().__init__(db_name)
    
    def update_request_review(self, student_id, task_id):
        """
            Updates the status of a review request in the Task_Review table

            Parameters:
                student_id (int): The ID of the student being queried
                task_id (int): The ID of the task being queried
        """
        
        query = f"""
            UPDATE Student_Task
            SET REVIEW_SUBMITTED = 1
            WHERE STUDENT_ID = {student_id}
            AND TASK_ID = {task_id}
        """        

        self.run_query(query)

        query = f"""
            INSERT INTO Task_Review(STUDENT_ID, TASK_ID) VALUES ({student_id}, {task_id})
        """

        self.run_query(query)

    def get_tasks(self, student_id: str) -> list[StudentDashboardDTO]:
        """
            Retrieves task information for a student 

            Parameters:
                student_id (int): ID for the student whose tasks are being queried
            
            Returns:
                dictionary of student and task information
        """

        # Query the Course, Student and Student_Task table to get the required information
        query = f"""
            SELECT ST.STUDENT_ID, ST.TASK_ID, T.TASK_NUMBER,
                    C.COURSE_NAME, T.NAME, ST.GRADE, ST.REVIEW_SUBMITTED,
                    T.FOLDER_LINK, S.FOLDER_LINK
            FROM Course C, Student S, Student_Task ST
            INNER JOIN Task T ON ST.TASK_ID = T.TASK_ID
            WHERE ST.STUDENT_ID = {student_id}
            AND S.STUDENT_ID = ST.STUDENT_ID
            AND C.COURSE_ID = S.COURSE_ID
        """       
        data = self.run_query(query)
        keys = ["student_id", "task_id", "task_number", "course", "topic", "review_score",
                "review_status", "content_download_link", "student_folder_upload_link"]
        
        student_list = self.convert_tuple_to_dict(keys, data)
        student_object_list = [StudentDashboardDTO.parse_obj(review) for review in student_list]
        return student_object_list

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
