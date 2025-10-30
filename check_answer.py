# 模範解答を管理するファイル
from typing import List, Union

# 正解時に返す定数
EBIFLY_CORRECT = "EBIFLY"
HAMIGAKI_CORRECT = "HAMIGAKI"

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
    
    # どちらでもない場合
    return False

def get_all_answers() -> List[str]:
    """
    全ての模範解答を取得
    
    Returns:
        List[str]: 模範解答のリスト
    """
    return EBIFLY_ANSWERS + HAMIGAKI_ANSWERS

