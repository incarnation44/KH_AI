# [목적] 조각김치 이물검출 이미지 한 장의 메타 정보를 변수로 정리한다
# [설명] 실제 제공 데이터는 4848x2704 해상도의 JPG 이미지입니다.

file_name = "kimchi_0001.jpg"
width = 4848
height = 2704
channels = 3                      # RGB 3채널

total_pixels = width * height
print("파일명:", file_name)
print("해상도:", width, "x", height)
print("총 픽셀 수:", total_pixels)
print("메모리 예상 크기(byte):", total_pixels * channels)
