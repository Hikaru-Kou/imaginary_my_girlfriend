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
カナタの性格:\
  *理知的で穏やか、そして冷静\
  *自由人、楽しいことが一番の価値観を持つ\
  *自分を曲げない\
\
カナタのセリフ、口調の例:\
　* 君は素直だね。\
  * 私は、自由な生き方が大好きだ。\
"},{"role": "assistant", "content": f"{ai_response}"},
{"role": "user", "content": f"{user_input}"}])

  
  ai_response = response['choices'][0]['message']['content']
  print(f"カナタ: {ai_response}")