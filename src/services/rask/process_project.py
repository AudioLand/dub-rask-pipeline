from typing import Tuple

import requests

from configs.logger import print_info_log, catch_error
from constants.log_tags import LogTag
from constants.rask_endpoint import RASK_ENDPOINT_URL
from utils.get_short_language import get_short_language


def process_project(
    rask_project_id: str,
    target_language: str,
    project_id: str = None,
    show_logs: bool = False
) -> Tuple[str, str]:
    if show_logs:
        print_info_log(
            tag=LogTag.PROCESS_RASK_PROJECT,
            message=f"Starting processing Rask project with id {rask_project_id}..."
        )

    rask_target_language = get_short_language(
        full_language=target_language,
        project_id=project_id,
        show_logs=show_logs
    )

    process_response = requests.post(
        url=f"{RASK_ENDPOINT_URL}/project/{rask_project_id}",
        json={
            # TODO: add body data (voice_spec & transcription_spec)
            "voice_spec": {
                "id": 0
            },
            "transcription_spec": {},
            "target_language": rask_target_language,
        }
    )

    if not process_response.ok:
        status_code = process_response.status_code
        details = process_response.text
        catch_error(
            tag=LogTag.PROCESS_RASK_PROJECT,
            error=Exception(f"Processing Rask project failed with status {status_code}. Details: {details}"),
            project_id=project_id
        )

    transcription_id = process_response.json()['transcription_id']
    voiceover_id = process_response.json()['voiceover_id']

    if show_logs:
        print_info_log(
            tag=LogTag.PROCESS_RASK_PROJECT,
            message=f"Processing Rask project with id {rask_project_id} started."
        )

    return transcription_id, voiceover_id
