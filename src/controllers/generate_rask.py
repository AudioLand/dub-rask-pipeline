from datetime import datetime

from configs.logger import print_info_log, catch_error
from constants.log_tags import LogTag
from constants.voiceover_state import VoiceoverState
from models.project_status import ProjectStatus
from routers.dub import dub_router
from services.firebase.firestore.project import update_project_status_and_translated_link_by_id
from services.firebase.storage.get_file_url import get_file_url
from services.rask.create_project import create_project
from services.rask.get_voiceover_result import get_voiceover_result
from services.rask.process_project import process_project


@dub_router.get("/")
def generate_rask(
    project_id: str,
    target_language: str,
    voice_id: int,
    original_file_location: str,
    organization_id: str,
    user_email: str,
):
    try:
        start_time = datetime.now()
        print_info_log(
            tag=LogTag.MAIN,
            message=f"Job Started! Processing project with id {project_id}..."
        )

        """Get file link in Firebase Storage"""

        original_file_url = get_file_url(
            storage_file_path=original_file_location,
            show_logs=True
        )

        """Create Rask project"""

        rask_project_id = create_project(
            name=project_id,
            url=original_file_url,
            project_id=project_id,
            show_logs=True
        )

        """Change project status to "translating"""

        print_info_log(
            tag=LogTag.MAIN,
            message="Updating project status to 'translating'..."
        )

        update_project_status_and_translated_link_by_id(
            project_id=project_id,
            status=ProjectStatus.TRANSLATING.value,
            translated_file_link="",
            show_logs=True
        )

        print_info_log(
            tag=LogTag.MAIN,
            message="Project status updated."
        )

        """Process Rask project"""

        transcription_id, voiceover_id = process_project(
            rask_project_id=rask_project_id,
            target_language=target_language,
            project_id=project_id,
            show_logs=True
        )

        """Long polling of project voiceover result state"""

        while True:
            print_info_log(
                tag=LogTag.MAIN,
                message="Pulling voiceover result state..."
            )

            voiceover_state, voiceover_url = get_voiceover_result(
                voiceover_id=voiceover_id,
                project_id=project_id,
                show_logs=True
            )

            print_info_log(
                tag=LogTag.MAIN,
                message=f"Voiceover state is {voiceover_state}."
            )

            if voiceover_state == VoiceoverState.READY:
                break

            if voiceover_state == VoiceoverState.FAILED:
                catch_error(
                    tag=LogTag.MAIN,
                    error=Exception(f"Voiceover with id {voiceover_id} failed."),
                    project_id=project_id
                )

        """Change project status to "translated"""

        print_info_log(
            tag=LogTag.MAIN,
            message="Updating project status to 'translated'..."
        )

        translated_file_link = voiceover_url
        update_project_status_and_translated_link_by_id(
            project_id=project_id,
            status=ProjectStatus.TRANSLATED.value,
            translated_file_link=translated_file_link,
            show_logs=True
        )

        print_info_log(
            tag=LogTag.MAIN,
            message="Project status updated."
        )

        """Update user used tokens in seconds"""

        print_info_log(
            tag=LogTag.MAIN,
            message="Updating user used tokens..."
        )

        # TODO: get used tokens for project
        # update_user_tokens(
        #     organization_id=organization_id,
        #     tokens_in_seconds=used_tokens_in_seconds,
        #     project_id=project_id
        # )

        print_info_log(
            tag=LogTag.MAIN,
            message="User used tokens updated."
        )

        """Send email to user about successful project completion"""

        # print_info_log(
        #     tag=LogTag.MAIN,
        #     message="Sending email to user about successful project completion..."
        # )
        #
        # send_email_with_api(
        #     user_email=user_email,
        #     email_template=EmailTemplate.SuccessfulProjectCompletion,
        # )
        #
        # print_info_log(
        #     tag=LogTag.MAIN,
        #     message="Email was sent to user successfully."
        # )

        end_time = datetime.now()
        time_difference = end_time - start_time

        print_info_log(
            tag=LogTag.MAIN,
            message=f"Job Done! Project translation time: {time_difference}"
        )

        return {"status": "it is working!!!"}

    except Exception as e:
        catch_error(
            tag=LogTag.MAIN,
            error=e,
            project_id=project_id
        )


if __name__ == "__main__":
    test_user_id = "z8Z5j71WbmhaioUHDHh5KrBqEO13"
    test_project_id = "LTsxu89FFAtLjP9ad0qd"
    test_file_name = "test-video-1min.mp4"
    test_target_language = "Russian"
    test_voice_id = 165
    test_original_file_location = f"{test_user_id}/{test_project_id}/{test_file_name}"
    test_organization_id = "ZXIFYVhPAMql66Vg5f5Q"
    test_user_email = "your@email.com"
    generate_rask(
        project_id=test_project_id,
        target_language=test_target_language,
        voice_id=test_voice_id,
        original_file_location=test_original_file_location,
        organization_id=test_organization_id,
        user_email=test_user_email
    )
