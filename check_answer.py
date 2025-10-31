# 模範解答を管理するファイル
from typing import List, Union

# 正解時に返す定数
EBIFLY_CORRECT = "EBIFLY"
HAMIGAKI_CORRECT = "HAMIGAKI"
BOMB1_CORRECT = "BOMB1"
BOMB2_CORRECT = "BOMB2"
BOMB3_CORRECT = "BOMB3"
BOMB4_CORRECT = "BOMB4"

# 模範解答のリスト（固定）
EBIFLY_ANSWERS = [
    "えびふりゃー",
    "エビフリャー",
    "エビフリャ～",
    "えびふりゃ～"
]

HAMIGAKI_ANSWERS = [
    "はみがき",
    "ハミガキ"
]

BOMB1_ANSWERS = [
    "you still have 3 questions lol"
]

BOMB2_ANSWERS = [
    "7","７"
]

BOMB3_ANSWERS = [
    "48",
    "４８"
]

BOMB4_ANSWERS = [
    "335",
    "３３５"
]

def check_answer(user_input: str) -> Union[str, bool]:
    """
    ユーザーの入力が模範解答に含まれているかチェック
    
    Args:
        user_input (str): ユーザーが入力した文字列
        
    Returns:
        Union[str, bool]: エビフライ正解ならEBIFLY_CORRECT、歯磨き正解ならHAMIGAKI_CORRECT、不正解ならFalse
    """
    # 前後の空白を削除して比較
    cleaned_input = user_input.strip()
    
    # エビフライの模範解答かチェック
    if cleaned_input in EBIFLY_ANSWERS:
        return EBIFLY_CORRECT
    
    # 歯磨きの模範解答かチェック
    if cleaned_input in HAMIGAKI_ANSWERS:
        return HAMIGAKI_CORRECT
    
    # BOMB1の模範解答かチェック
    if cleaned_input in BOMB1_ANSWERS:
        return BOMB1_CORRECT
    
    # BOMB2の模範解答かチェック
    if cleaned_input in BOMB2_ANSWERS:
        return BOMB2_CORRECT
    
    # BOMB3の模範解答かチェック
    if cleaned_input in BOMB3_ANSWERS:
        return BOMB3_CORRECT
    
    # BOMB4の模範解答かチェック
    if cleaned_input in BOMB4_ANSWERS:
        return BOMB4_CORRECT
    
    # どれでもない場合
    return False

def get_all_answers() -> List[str]:
    """
    全ての模範解答を取得
    
    Returns:
        List[str]: 模範解答のリスト
    """
    return EBIFLY_ANSWERS + HAMIGAKI_ANSWERS + BOMB1_ANSWERS + BOMB2_ANSWERS + BOMB3_ANSWERS + BOMB4_ANSWERS

