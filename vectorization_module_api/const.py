from pathlib import Path
from ..shared.utils.fileutils import create_dirs_if_not, create_file_if_not
from ..config.base import ENV, BASE_DIR, XACCEL_PREFIX, API_DATA_FOLDER
import torch

DEMO_NAME = "vectorization"

# Path to extraction/ folder
DEMO_DIR = BASE_DIR / "app" / DEMO_NAME
LIB_PATH = DEMO_DIR / "lib"

VEC_QUEUE = "queue4"  # see docker-confs/supervisord.conf

VEC_DATA_FOLDER = API_DATA_FOLDER / DEMO_NAME
# VEC_XACCEL_PREFIX = Path(ENV("EXT_XACCEL_PREFIX", default="/media/vectorization-results"))
VEC_RESULTS_PATH = VEC_DATA_FOLDER / "results"

IMG_PATH = VEC_DATA_FOLDER / "documents" / "images"
ANNO_PATH = VEC_RESULTS_PATH
MODEL_PATH = VEC_DATA_FOLDER / "models"

create_dirs_if_not([IMG_PATH, MODEL_PATH])
torch.hub.set_dir(f'{BASE_DIR}/.cache')

DEFAULT_EPOCHS = "0045"
