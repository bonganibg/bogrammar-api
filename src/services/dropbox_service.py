import dropbox
from dropbox.files import WriteMode, GetTemporaryLinkResult
from dropbox.exceptions import ApiError, AuthError

class DropboxService:
    def __init__(self, token) -> None:
        self.token = token
    
    def get_dropbox_connection(self):
        """
            Set up connection to dropbox client

            Return: 
                Dropbox connection
        """

        with dropbox.Dropbox(self.token) as dbx:
            try:
                dbx.users_get_current_account()
                return dbx
            except AuthError:
                return None
                
    def write_file_to_dropbox(self, file, upload_path: str, dbx: dropbox.Dropbox):
        """
            upload file to dropbox path

            Parameters: 
                file (File): file to be uploaded
                upload_path (str): path to folder where file will be saved
                dbx (Dropbox): Dropbox connection object
        """

        try:
            dbx.files_upload(file, upload_path, mode=WriteMode('overwrite'))
            return True
        except ApiError:
            return False
        
    def read_file_from_dropbox(self, file_path: str, dbx: dropbox.Dropbox) -> GetTemporaryLinkResult:
        """
            Get file download link from dropbox

            Parameters:
                file_path (str): Path to dropbox file including the file extension
                dbx (Dropbox): Dropbox connection object

            Returns:
                GetTemporaryLinkResult object containing download link
        """

        # Make sure folder path starts with a forward slash
        if (file_path[0] != '/'):
            file_path = f"/{file_path}"

        return dbx.files_get_temporary_link(file_path) 