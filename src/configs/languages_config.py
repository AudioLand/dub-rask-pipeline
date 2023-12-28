import json
import os

from configs.logger import catch_error
from constants.log_tags import LogTag

# Get the absolute path to the current file
current_file = __file__

# Get the absolute path to the folder containing the current file
current_folder_path = os.path.dirname(os.path.abspath(current_file))

# Absolute path to rask-languages config
languages_config_path = f"{current_folder_path}/rask-languages.json"

try:
    languages_config_file = open(languages_config_path, "r")
    # Convert dict to list of TargetVoices
    languages_config: dict = json.load(languages_config_file)
    languages_config_file.close()
except Exception as e:
    catch_error(
        tag=LogTag.RASK_LANGUAGES_CONFIG,
        error=e,
    )
