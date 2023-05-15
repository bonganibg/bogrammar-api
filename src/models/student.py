from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile

class StudentDashboardDTO(BaseModel):
    StudentID: int
    TaskID: int
    TaskNumber: int
    Course: str
    Topic: str
    ReviewScore: str
    ReviewStatus: str
    ContentDownloadLink: str
    StudentFolderUploadLink: str

class StudentReviewRequest(BaseModel):
    StudentID: int
    TaskID: int