from configs.firebase import bucket
from configs.logger import print_info_log
from constants.log_tags import LogTag


def get_file_url(
    storage_file_path: str,
    show_logs: bool = False
):
    if show_logs:
        print_info_log(
            tag=LogTag.UPLOAD_BLOB,
            message=f"Get url to file with path: {storage_file_path}"
        )

    blob = bucket.blob(storage_file_path)
    blob.make_public()
    public_url = blob.public_url

    if show_logs:
        print_info_log(
            tag=LogTag.UPLOAD_BLOB,
            message=f"Url to file: {public_url}"
        )

    return public_url
