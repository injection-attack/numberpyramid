# print(' '+' '+' '+'1') # 줄 수당 앞에 ' '공백 추가
# print(' '+' '+'123'+' '+' ') # 줄 수당 양쪽으로 공백 하나씩 추가
# print(' ' +'12345'+' ') # 줄 수당 양쪽으로 공백 하나씩 추가
# print(1234567)

from flask import Flask, render_template, request

app = Flask(__name__)

def generate_pyramid(num_rows):
    pyramid = []
    for i in range(1, num_rows + 1):
        row = ' ' * (num_rows - i)
        for j in range(1, 2 * i):
            row += str(j)
        row += ' ' * (num_rows - i)
        pyramid.append(row)
    return pyramid

@app.route('/', methods=['GET', 'POST'])
def pyramid_number_rows():
    if request.method == 'POST':
        num_rows = int(request.form['숫자열'])
        pyramid = generate_pyramid(num_rows)
        return render_template('pyramid.html', 피라미드=pyramid, 숫자열=num_rows)
    return render_template('pyramid.html')

#배포판 마지막 코드는 좀 다르다!
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
