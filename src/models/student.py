from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile

class StudentDashboardDTO(BaseModel):
    student_id: int
    task_id: int
    task_number: int
    course: str
    topic: str
    review_score: str
    review_status: bool
    content_download_link: str
    student_folder_upload_link: str

class StudentReviewRequest(BaseModel):
    student_id: int
    task_id: int