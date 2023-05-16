from fastapi import APIRouter, File, UploadFile, HTTPException
from src.repositories.student_repository import Student
from src.services.dropbox_service import DropboxService
from dropbox.files import GetTemporaryLinkResult
from src.models.student import StudentDashboardDTO, StudentReviewRequest
import os
from dotenv import load_dotenv
load_dotenv()


router = APIRouter(
    prefix="/student",
    tags=["student"]
)

student_repo = Student(os.getenv("DATABASE_NAME"))
dbs = DropboxService(os.getenv("DBX_TOKEN"))

@router.post("/review/request", status_code=201)
async def request_review(review: StudentReviewRequest):
    student_repo.update_request_review(review.student_id, review.task_id)
    print(review)
    return

@router.get("/{student_id}/dashboard", status_code=200)
async def get_dashboard(student_id) -> list[StudentDashboardDTO]:                                                                                                                                                                                                                                   
    
    dashboard =  student_repo.get_tasks(student_id)
    
    return dashboard

@router.get("/task", status_code=200)
async def get_task_content(file_path: str):
    dbx = dbs.get_dropbox_connection()
    response = dbs.read_file_from_dropbox(file_path, dbx)

    if (response == None):
        raise HTTPException(status_code=404, detail=f'{file_path} was not found')
    
    return response

@router.post("/task", status_code=201)
async def upload_task(file_path: str, file: UploadFile):
    print('hello')
    dbx = dbs.get_dropbox_connection()
    upload_file = await file.read(1024)

    dbs.write_file_to_dropbox(upload_file, file_path, dbx)


