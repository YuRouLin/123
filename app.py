from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')#首頁
def form():
    return render_template('input_data.html')

@app.route('/submit_form', methods=['POST'])
def handle_form():
    id_number = request.form.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    email = request.form.get('email')

    # Validate ID number (assuming 台灣ID)
    if len(id_number)!=10:                        #1. 確認身份證號碼長度是否為10。
        return "身分證號碼應該為10碼", 400
    if not id_number[0].isalpha():                #2. 確認第一個字元是否為英文字母
        return "第一個字元應該為英文字母碼", 400
        
    if not id_number[1:].isdigit():               #3. 確認後九個字元是否為數字
        return "身分證號碼後九碼應為數字", 400
        
   def validate_id_number(id_number):
    # 將英文字母轉換為對應的數字
    first_letter_num = ord(id_number[0]) - ord('A') + 10

    # 將轉換後的兩位數字分別乘以1和9
    total = first_letter_num * 1 + first_letter_num * 9

    # 將第二個到第九個數字分別乘以8 7 6 8 4 3 2 1
    for i in range(1, 9):
        total += int(id_number[i]) * (9 - i)

    # 加上最後一個數字
    total += int(id_number[-1])

    # 如果最後的結果可以被10整除，則這個身分證號碼就是正確的
    return total % 10 == 0

    if validate_id_number(id_number):
    print("這是一個正確的身分證號碼。")
    else:
    print("這是一個錯誤的身分證號碼。")





    
    # Validate name (assuming it's alphabetic)
    if not re.match(r'^[A-Za-z\s]+$', name):
        return "Invalid name", 400

    # Validate gender
    if gender not in ['Male', 'Female']:
        return "Invalid gender", 400

    # Validate email
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return "Invalid email", 400

    return "All entries are valid", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Listen on all available network interfaces and port 80
