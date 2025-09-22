# シンプルなデコレータの実演

# 1. シンプルなデコレータ
def my_decorator(func):
    def wrapper():
        print("関数実行前")
        func()
        print("関数実行後")
    return wrapper

# 2. デコレータを使わない普通の関数
def normal_function():
    print("普通の関数です")

# 3. デコレータを使った関数
@my_decorator
def decorated_function():
    print("デコレータが付いた関数です")

# 実行部分
if __name__ == "__main__":
    print("=== シンプルなデコレータの実演 ===\n")
    
    print("1. 普通の関数:")
    normal_function()
    print()
    
    print("2. デコレータが付いた関数:")
    decorated_function()
    print()
    
    print("=== 終了 ===")
