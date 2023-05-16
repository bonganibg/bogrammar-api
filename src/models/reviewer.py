from pydantic import BaseModel

class ReviewBacklogDTO(BaseModel):
    review_id: str
    student_name: str
    student_number: str
    folder_link: str
    course: str
    task: str
    task_folder_link: str
    
class ReviewScoreDTO(BaseModel):
    score: int
    review_id: int