from enum import Enum


class LogTag(Enum):
    TEST_ERROR = "test_error"
    TEST_INFO = "test_info"

    MAIN = "main"
    TTS_CONFIG = "tts_config"
    DOWNLOAD_BLOB = "download_blob"
    UPDATE_PROJECT = "update_project"
    UPLOAD_BLOB = "upload_blob"
    SPEECH_TO_TEXT = "speech_to_text"
    WHISPER_ENDPOINT_REQUEST = "whisper_endpoint_request"
    WHISPER_ENDPOINT_RESPONSE = "whisper_endpoint_response"
    SPLIT_TEXT_TO_CHUNKS = "split_text_to_chunks"
    TRANSLATE_TEXT_CHUNK_WITH_GPT = "translate_text_chunk_with_gpt"
    TRANSLATE_TEXT = "translate_text"
    COMBINE_TEXT_SEGMENTS = "combine_text_segments"
    TEXT_TO_SPEECH = "text_to_speech"
    GET_VOICE_BY_ID = "get_voice_by_id"
    ELEVENLABS_PROVIDER = "elevenlabs_provider"
    MICROSOFT_PROVIDER = "microsoft_provider"
    OVERLAY_AUDIO = "overlay_audio"
    UPDATE_USER_TOKENS = "update_user_tokens"

    CREATE_RASK_PROJECT = "create_rask_project"
    PROCESS_RASK_PROJECT = "process_rask_project"
    GET_VOICEOVER_RESULT = "get_voiceover_result"
    RASK_LANGUAGES_CONFIG = "rask_languages_config"
    GET_SHORT_LANG = "get_short_lang"
