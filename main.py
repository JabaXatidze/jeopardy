from flask import Flask
app = Flask(__name__, static_url_path='', static_folder='static')

data = [
  {
    "id": 1,  
    "name": "სრუტეები",
    "questions": [
      {
        "question": "ეს სრუტეები აკავშირებს ერთმანეთთან ხმელთაშუა და შავ ზღვებს.",
        "answer": "ბოსფორი და დარდანელი",
      },
      {
        "question":
          "ამ სრუტის ერთ მხარეს მდებარეობს ესპანური ქალაქი სეუტა, მეორე მხარეს კი ამ სრუტის სახელის მქონე დასახლება. მისი სახელი არაბულიდან ითარგმნება, როგორც “ტარიქის მთა”",
        "answer": "გიბრალტარი",
      },
    ],
  },
  {
    "id": 2,
    "name": "კინოციტატები",
    "questions": [
      {
        "question":
          "მერილინ ლოუელი: რატომ 13? ჯიმ ლოუელი: იმიტომ, რომ 12-ს მოსდევს",
        "answer": "აპოლო 13",
      },
      {
        "question":
          "ჰარი: მხოლოდ მცირე დახმარება, ღმერთო, სულ ესაა რასაც გთხოვ! მაქსი: ვფიქრობ, რომ მასთან საკმაოდ ახლოს ვართ. მას უნდა ესმოდეს შენი",
        "answer": "არმაგედონი",
      },
    ],
  },
]


# @app.route('/')
# def hello_world():
#     return app.send_static_file('JEOPARDY.html')

# @app.route('/hello')
# def hello_tato():
#     return '<h1>Hello, Tato!</h1>'

@app.route('/question/<topic_id>/<question_id>')
def get_question(topic_id, question_id):
    return { 
        "question": data[int(topic_id)]["questions"][int(question_id)]
    }

app.run(debug=True)