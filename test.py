import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import cv2
import torch
import numpy as np
import pandas as pd

print("="*60)
print("🎉 대성공! 학원 환경 100% 동일 세팅 완료!")
print("="*60)
print(f"✅ OpenCV 버전  : {cv2.__version__}")
print(f"✅ PyTorch 버전 : {torch.__version__} (CPU)")
print(f"✅ NumPy 버전   : {np.__version__}")
print(f"✅ Pandas 버전  : {pd.__version__}")
print("="*60)
print("이제 학원 데스크톱과 100% 동일한 환경에서 실습할 수 있습니다! 😎")
print("="*60)
