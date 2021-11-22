from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tasks

token = "토큰입력"
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    """
    대화방이 처음 열리면, 자동으로 호출되는 함수
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="안녕 나는 dlcksemf_bot이야. 만나서 반가워."
    )

def echo(update, context):
    received_text: str = update.message.text

    if tasks.ya.check_available(received_text):
        response_text = tasks.ya.make_response(received_text)
    elif tasks.naver_search.check_available(received_text):
        response_text = tasks.naver_search.make_response(received_text)
    else:
        response_text = "지원하는 명령입니다."

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response_text)

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(
    Filters.text & (~Filters.command),
    echo,
)

dispatcher.add_handler(echo_handler)

updater.start_polling()


# bot = telegram.Bot(token)
# # info = bot.getMe()
# # pprint.pprint(info)
# # resp = bot.getUpdates()
# # pprint.pprint(resp)
# chat_id = 2124512764
# bot.sendMessage(chat_id=chat_id, text="안녕 나는 봇이야")

