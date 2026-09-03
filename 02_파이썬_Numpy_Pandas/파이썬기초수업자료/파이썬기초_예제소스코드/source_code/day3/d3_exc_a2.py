# [목적] 잘못된 입력을 받아도 다시 물어보며 계속 진행한다
# [설명] while과 try를 결합한 입력 검증 패턴입니다.

def get_valid_threshold(inputs):
    """실습을 위해 입력값 목록을 순서대로 사용"""
    for raw in inputs:
        print(f"신뢰도 임계값(0~1) 입력: {raw}")
        try:
            value = float(raw)
        except ValueError:
            print("  -> 숫자가 아닙니다. 다시 입력하세요.\n")
            continue

        if value < 0 or value > 1:
            print("  -> 0~1 사이 값이어야 합니다. 다시 입력하세요.\n")
            continue

        print(f"  -> 임계값 {value} 설정 완료\n")
        return value
    return 0.7      # 모두 실패하면 기본값

th = get_valid_threshold(["abc", "1.5", "-0.2", "0.75"])
print("최종 적용 임계값:", th)
