import subprocess
import shlex
from pathlib import Path
import logging

BASE_DIR = Path(__file__).parent
logger = logging.getLogger(__name__)


def download_pretrained_model():
    """
    Downloads pretrained model if it does not already exist.
    the model file is downloaded from github releasee 0.0.1-dev
    Returns:
        bool: True if the model was successfully downloaded or already exists, False otherwise.
    """
    path = BASE_DIR / "face_detection/detection/sfd/s3fd.pth"
    if path.exists():
        return True
    try:
        subprocess.run(
            shlex.split(
                f"wget  https://github.com/ibleducation/ibl-wav2lip/releases/download/0.0.1-dev/s3fd.pth -O {str(path)}"
            ),
            cwd=BASE_DIR,
            check=True,
        )
        return True
    except Exception as e:
        logger.exception(e)
        return False


def download_checkpoint_file():
    """
    Downloads pretrained model if it does not already exist.
    the model file is downloaded from github releasee 0.0.1-dev
    Returns:
        bool: True if the model was successfully downloaded or already exists, False otherwise.
    """
    path = BASE_DIR / "checkpoints/wav2lip_gan.pth"
    if path.exists():
        return True
    try:
        subprocess.run(
            shlex.split(
                f"wget  https://github.com/ibleducation/ibl-wav2lip/releases/download/0.0.1-dev/wav2lip_gan.pth -O {str(path)}"
            ),
            cwd=BASE_DIR,
            check=True,
        )
        return True
    except Exception as e:
        logger.exception(e)
        return False


if __name__ == "__main__":
    download_pretrained_model()
    download_checkpoint_file()
