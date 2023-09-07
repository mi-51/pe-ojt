# スタートと終了の数値セット
start_num = 1
end_num = 100

# 1から100まで繰り返し開始
for i in range(start_num, end_num + 1):
  # 3かつ5の倍数時の処理
  if i % 3 == 0 and i % 5 == 0:
    print(str(i) + '：FizzBuzz')

  # 3の倍数時の処理
  elif i % 3 == 0:
    print(str(i) + '：Fizz')

  # 5の倍数時の処理
  elif i % 5 == 0:
    print(str(i) + '：Buzz')

  # すべての条件に当てはまらない場合の処理
  else:
    print(str(i))