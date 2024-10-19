# import sys
# sys.path.insert(0, '/home/anna/python/VK/llm-course-2024-autumn/Homework/01/scripts')

# from tokenizer import ByteTokenizer
# from model import Model
# from dataset import MyDataset
# from collator import Collator
# from trainer import Trainer
# from generation import generate

from scripts.tokenizer import BpeTokenizer
from .model import Model
from .dataset import MyDataset
from .collator import Collator
from .trainer import Trainer
from .generation import generate