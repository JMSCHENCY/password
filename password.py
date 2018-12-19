# 最多輸入3次
# 如果正確，就印出“登入成功！”
# 如果不正確，就印出“密碼錯誤！ 還有＿次機會！”

password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
    i = i - 1
    pwd = input('請輸入密碼： ')
    if pwd == password:
        print('登入成功！')
        break
    else:
        if i > 0:
            print('密碼錯誤！ 還有', i, '次機會！')
        elif i == 0:
            print('已使用完三次錯誤機會，請至分行變更密碼！')
            break