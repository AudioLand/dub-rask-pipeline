from configs.languages_config import languages_config
from configs.logger import catch_error
from constants.log_tags import LogTag


def get_short_language(full_language: str, project_id: str, show_logs: bool = False):
    try:
        short_language = languages_config[full_language.lower()]
        return short_language

    except Exception as e:
        catch_error(
            tag=LogTag.GET_SHORT_LANG,
            error=e,
            project_id=project_id
        )


if __name__ == "__main__":
    test_full_language = "Russian"
    test_project_id = "LTsxu89FFAtLjP9ad0qd"
    short_language = get_short_language(
        full_language=test_full_language,
        project_id=test_project_id
    )
    print(short_language)
