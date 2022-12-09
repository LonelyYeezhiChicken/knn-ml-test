import argparse


def main():
    # 創建解析器
    parser = argparse.ArgumentParser(description='簡單的 Python 主控台應用程式')

    # 添加參數
    parser.add_argument('--name', type=str, help='您的名字')

    # 解析參數
    args = parser.parse_args()

    # 輸出結果
    print(f'嗨，{args.name}！')


if __name__ == '__main__':
    main()
