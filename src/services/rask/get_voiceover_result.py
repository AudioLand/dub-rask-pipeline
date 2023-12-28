import requests

from configs.logger import catch_error, print_info_log
from constants.log_tags import LogTag
from constants.rask_endpoint import RASK_ENDPOINT_URL


def get_voiceover_result(
    voiceover_id: str,
    project_id: str,
    show_logs: bool = False
):
    if show_logs:
        print_info_log(
            tag=LogTag.GET_VOICEOVER_RESULT,
            message=f"Getting voiceover result with id {voiceover_id}..."
        )

    voiceover_result_response = requests.get(url=f"{RASK_ENDPOINT_URL}/voiceover/{voiceover_id}/result")

    if not voiceover_result_response.ok:
        status_code = voiceover_result_response.status_code
        details = voiceover_result_response.text
        catch_error(
            tag=LogTag.GET_VOICEOVER_RESULT,
            error=Exception(f"Voiceover failed with status {status_code}. Details: {details}"),
            project_id=project_id
        )

    voiceover_state = voiceover_result_response.json()['state']
    voiceover_url = voiceover_result_response.json()['url']

    if show_logs:
        print_info_log(
            tag=LogTag.GET_VOICEOVER_RESULT,
            message=f"Processing Rask project with id {voiceover_id} started."
        )

    return voiceover_state, voiceover_url
