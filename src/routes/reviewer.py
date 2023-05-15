import os
from fastapi import APIRouter
from src.repositories.reviewer_repository import Reviewer
from src.services.dropbox_service import DropboxService
from dropbox.files import GetTemporaryLinkResult
from src.models.reviewer import ReviewBacklogDTO, ReviewScoreDTO
from dotenv import load_dotenv
load_dotenv()


router = APIRouter(
    prefix="/reviewer",
    tags=["reviewer"]
)

TOKEN = os.getenv('DBX_TOKEN')

reviewer_repo = Reviewer(os.getenv('DATABASE_NAME'))
dbs = DropboxService(TOKEN)

@router.get("/backlog")
async def get_backlog() -> list[ReviewBacklogDTO]:
    backlog = reviewer_repo.get_review_backlog()

    return backlog

@router.put("/{review_id}", status_code=201)
async def submit_review(review: ReviewScoreDTO):
    reviewer_repo.update_review_score(review.ReviewID, review.Score)
    print(review.Score)
    return

@router.get("/work/{folder_link}")
async def get_work_folder(folder_link: str) -> str:
    dbx = dbs.get_dropbox_connection()
    response: GetTemporaryLinkResult.link = dbs.read_file_from_dropbox(folder_link, dbx)
    
    return {
        "Link": f"{response.link}"
    }