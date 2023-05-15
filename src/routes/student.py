from fastapi import APIRouter, File, UploadFile
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

@router.post("/review/request", status_code=204)
async def request_review(review: StudentReviewRequest):
    student_repo.update_request_review(review.StudentID, review.TaskID)
    print(review)
    return

@router.get("/{student_id}/dashboard")
async def get_dashboard(student_id) -> list[StudentDashboardDTO]:                                                                                                                                                                                                                                   
    
    dashboard =  student_repo.get_tasks(student_id)
    
    return dashboard

@router.get("/task")
async def get_task_content(content_link: str):
    dbx = dbs.get_dropbox_connection()
    response: GetTemporaryLinkResult.link = dbs.read_file_from_dropbox(content_link, dbx)

    return {
        "Link": f"{response.link}"
    }

@router.post("/task")
async def upload_task(file_data: str, file: UploadFile):
    dbx = dbs.get_dropbox_connection()
    upload_file = await file_data.read(1024)

    dbs.write_file_to_dropbox(upload_file, file_data, dbx)


