import json

import requests

from configs.logger import catch_error, print_info_log
from constants.log_tags import LogTag
from constants.rask_endpoint import RASK_ENDPOINT_URL


def create_project(name: str, url: str, project_id: str = None, show_logs: bool = False) -> str:
    if show_logs:
        print_info_log(
            tag=LogTag.CREATE_RASK_PROJECT,
            message="Creating Rask project..."
        )

    rask_project_data = {
        # Use json.dumps to convert obj to str
        # e.g.: "project": '{ "name": ... }'
        "project": json.dumps({
            "name": name,
            "url": url
        })
    }

    project_response = requests.post(
        url=f"{RASK_ENDPOINT_URL}/project/",
        data=rask_project_data,
    )

    if not project_response.ok:
        status_code = project_response.status_code
        details = project_response.text
        catch_error(
            tag=LogTag.CREATE_RASK_PROJECT,
            error=Exception(f"Creating Rask project failed with status {status_code}. Details: {details}"),
            project_id=project_id
        )

    rask_project_id = project_response.json()['project_id']

    if show_logs:
        print_info_log(
            tag=LogTag.CREATE_RASK_PROJECT,
            message=f"Rask project created with id: {rask_project_id}."
        )

    return rask_project_id


if __name__ == "__main__":
    test_rask_project_id = create_project(
        name="test-dub",
        url="https://firebasestorage.googleapis.com/v0/b/audioland-dub.appspot.com/o/z8Z5j71WbmhaioUHDHh5KrBqEO13%2FLTsxu89FFAtLjP9ad0qd%2Ftest-video-1min.mp4?alt=media&token=38897394-985d-48da-8dc7-775c1bc387c1",
        show_logs=True
    )
