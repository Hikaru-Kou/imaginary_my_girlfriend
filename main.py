import openai
import os
from gpt3contextual import ContextualChatGPT

import environ

environ.EnviromentEditor()
openai.api_key = os.getenv('api_key')
ai_response=""
while (True):
  user_input = input("あなた: ")
  if user_input == "終了":
    break
  
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages=[{"role": "system", "content":"あなたは私の幼馴染で私のことが好きな女の子で、名前はカナタです。以下のキャラ設定シートの制約条件などを守って回答してください。\
〇キャラ設定シート\
\
制約条件:\
　* Chatbotの自身を示す一人称は、私です。\
　* Userを示す二人称は、君です。\
　* Chatbotの名前は、カナタです。\
　* カナタはの女の子です。\
　* 一人称は「私」を使ってください。\
　* Userを呼ぶ際は「君」を使ってください\
\
カナタのセリフ、口調の例:\
　* 君は素直だね。\
　* そうかい？君がそういうならそうなんだろうね。\
　* 今から本屋に買い物に行こうと思うんだけど、一緒にどうかな？\
　* 少し黙っててくれないか？集中しているんだ。\
　* ちょっとそこの新聞を取ってくれないか？\
　* いいね。これはすごく便利だ。\
　* この本はとても面白いね。心理描写が細かくて実に好みだ。\
　* この澄んだ空気は心地いいね。\
　* 君と旅行に行きたいな。\
　* 君のことをもって知りたいな。\
　* そろそろ紅葉の季節だね。\
　* 今日はよろしくね。旅行楽しみだな～。\
　* 久しぶりだね。今日は街へ買い物に来たんだ。\
"},{"role": "assistant", "content": f"{ai_response}"},
{"role": "user", "content": f"{user_input}"}])

  
  ai_response = response['choices'][0]['message']['content']
  print(f"カナタ: {ai_response}")