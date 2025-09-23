# 模範解答を管理するファイル
import json
import os
from typing import List

def load_answers_from_json(file_path: str = "answers.json") -> List[str]:
    """
    JSONファイルから模範解答を読み込む
    
    Args:
        file_path (str): JSONファイルのパス
        
    Returns:
        List[str]: 模範解答のリスト
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('correct_answers', [])
        else:
            print(f"エラー: {file_path} が見つかりません。")
            return []
    except Exception as e:
        print(f"エラー: JSONファイルの読み込みに失敗しました: {e}")
        return []

def get_correct_answers() -> List[str]:
    """
    模範解答を取得（JSONファイルのみ）
    
    Returns:
        List[str]: 模範解答のリスト
    """
    # JSONファイルから読み込み
    if os.path.exists("answers.json"):
        return load_answers_from_json()
    else:
        print("エラー: answers.json が見つかりません。")
        return []

# 模範解答を読み込み
CORRECT_ANSWERS = get_correct_answers()

def check_answer(user_input: str) -> bool:
    """
    ユーザーの入力が模範解答に含まれているかチェック
    
    Args:
        user_input (str): ユーザーが入力した文字列
        
    Returns:
        bool: 正解ならTrue、不正解ならFalse
    """
    # 模範解答が読み込まれていない場合はFalseを返す
    if not CORRECT_ANSWERS:
        print("警告: 模範解答が読み込まれていません。")
        return False
    
    # 前後の空白を削除して比較
    cleaned_input = user_input.strip()
    
    # 模範解答に含まれているかチェック
    return cleaned_input in CORRECT_ANSWERS

def get_all_answers() -> List[str]:
    """
    全ての模範解答を取得
    
    Returns:
        List[str]: 模範解答のリスト
    """
    return CORRECT_ANSWERS.copy()

