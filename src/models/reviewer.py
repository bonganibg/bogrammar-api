from pydantic import BaseModel

class ReviewBacklogDTO(BaseModel):
    ReviewID: str
    StudentName: str
    StudentNumber: str
    FolderLink: str
    Course: str
    Task: str
    TaskFolderLink: str
    
class ReviewScoreDTO(BaseModel):
    Score: int
    ReviewID: int