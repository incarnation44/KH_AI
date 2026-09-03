# [목적] 여러 값을 조합해 사람이 읽기 좋은 결과 리포트를 출력한다
# [설명] GUI 화면이나 로그 파일에 남길 문장을 이렇게 조립합니다.

file_name = "conveyor_0042.jpg"
class_name = "플라스틱·돌·금속"
confidence = 0.9237
inference_ms = 38.6
is_ng = True

verdict = "NG" if is_ng else "OK"      # 조건에 따라 값 고르기

line1 = f"[{verdict}] {file_name}"
line2 = f"  검출: {class_name} (신뢰도 {confidence:.1%})"
line3 = f"  처리시간: {inference_ms:.1f}ms ({1000/inference_ms:.1f} FPS)"

report = "\n".join([line1, line2, line3])
print(report)
