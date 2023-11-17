from .inference import main

from argparse import Namespace

import logging
from pathlib import Path
logger = logging.getLogger(__name__)

BASE_DIR = Path.cwd()


class Inference:
    """
    Wrapper class around inference cli module.
    """

    def __init__(
        self,
        face: str,
        audio: str,
        checkpoint_path: str = "wav2lip_gan.pth",
        outfile: str=str(BASE_DIR/'output.mp4'),
        static: bool = False,
        fps: float = 25.0,
        pads: list[int] = [0, 10, 0, 0],
        face_det_batch_size: int = 16,
        wav2lip_batch_size: int = 128,
        resize_factor: int = 1,
        crop: list[int] = [0, -1, 0, -1],
        box: list[int] = [-1, -1, -1, -1],
        rotate: bool = False,
        nosmooth: bool = False,
        img_size: int = 96
    ):
        """
        Initializes the class with the given parameters.
        Args:
            checkpoint_path (str): The path to the checkpoint.
            face (str): The path to the input face video.
            audio (str): The path to the input audio file.
            outfile (str): The path to the output video file.
            static (bool, optional): Whether to use a static image or not. Defaults to False.
            fps (float, optional): The frames per second of the output video. Defaults to 25.0.
            pads (list[int], optional): The padding values for the face in the output video. Defaults to [0, 10, 0, 0].
            face_det_batch_size (int, optional): The batch size for face detection. Defaults to 16.
            wav2lip_batch_size (int, optional): The batch size for wav2lip. Defaults to 128.
            resize_factor (int, optional): The resize factor for the input video. Defaults to 1.
            crop (list[int], optional): The cropping values for the input video. Defaults to [0, -1, 0, -1].
            box (list[int], optional): The bounding box coordinates for the face in the input video. Defaults to [-1, -1, -1, -1].
            rotate (bool, optional): Whether to rotate the output video or not. Defaults to False.
            nosmooth (bool, optional): Whether to apply smoothing to the output video or not. Defaults to False.
        Returns:
            None
        """
        checkpoint_path = str(Path(__file__).parent / "checkpoints" / checkpoint_path)
        self.args = Namespace(
            checkpoint_path=checkpoint_path,
            face=face,
            audio=audio,
            outfile=outfile,
            static=static,
            fps=fps,
            pads=pads,
            face_det_batch_size=face_det_batch_size,
            wav2lip_batch_size=wav2lip_batch_size,
            resize_factor=resize_factor,
            crop=crop,
            box=box,
            rotate=rotate,
            nosmooth=nosmooth,
            img_size=img_size,
        )

        if Path(self.args.face).is_file() and self.args.face.split('.')[1] in ['jpg', 'png', 'jpeg']:
            self.args.static = True

        self.check_required_files(checkpoint_path=checkpoint_path, )

    def check_required_files(self, checkpoint_path):
        if not Path(checkpoint_path).is_file():
            raise FileNotFoundError(f'Checkpoint file not found: {checkpoint_path}')
    

    def run(self) -> str:
        try:
            main(self.args)
        except Exception as e:
            logger.exception(e)
        return self.args.outfile
            
