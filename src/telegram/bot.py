from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from google.oauth2 import service_account
from googleapiclient.discovery import build
import logging

# Configuração do log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Caminho para o arquivo de credenciais
SERVICE_ACCOUNT_FILE = 'x'
SCOPES = ['x']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Inicializa o cliente da API do YouTube
youtube = build('youtube', 'v3', credentials=credentials)

# Função para verificar se o usuário é membro do canal do YouTube
def is_youtube_member(channel_id, user_id):
    try:
        request = youtube.membershipsLevels().list(
            part='snippet',
            filterByMemberChannelId=user_id
        )
        response = request.execute()
        return any(member['snippet']['channelId'] == user_id for member in response.get('items', []))
    except Exception as e:
        logging.error(f"Erro ao verificar membro no YouTube: {e}")
        return False

# Função para o comando /start
def start(update: Update, context):
    message = "Olá, que bom receber sua mensagem. Seja bem-vindo(a)!\nDigite /tutorial para aprender como acessar o Grupo VIP exclusivo para membros, a partir do nível Inspetor ou /comandos para ver os comandos disponíveis."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Função para o comando /tutorial
def tutorial(update: Update, context):
    message = ("Para ter acesso ao Grupo VIP, siga os passos abaixo para encontrar seu ID do YouTube:\n"
               "1. Acesse o site https://www.youtube.com/.\n"
               "2. Clique no ícone do seu perfil no canto superior direito.\n"
               "3. Selecione 'Seu canal' no menu.\n"
               "4. No seu canal, você encontrará o nome do seu canal. Esse é o seu ID do YouTube.\n\n"
               "Por favor, copie o nome do seu canal exatamente como está escrito, respeitando espaços, letras maiúsculas e minúsculas, e cole aqui para que possamos verificar sua assinatura.")
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Função para o comando /assinar
def assinar(update: Update, context):
    message = "Caso ainda não seja um membro a partir do nível Inspetor, faça sua assinatura e tenha acesso aos benefícios exclusivos para membros. Clique no link a seguir para acessar o canal e se inscrever:\n\nhttps://youtu.be/wnS1HYXQ0M4?si=0xYuVApptIAekZy_"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Função para o comando /suporte
def suporte(update: Update, context):
    message = "Por favor, entre em contato pelo Telegram com:\n\n@Suporteligacrypto ou @ComKaio"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Função para o comando /ajuda
def ajuda(update: Update, context):
    message = "Por favor, use o comando /tutorial para saber o passo a passo ou /suporte caso já tenha feito os outros comandos, mas ainda esteja com problemas."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Função para o comando /comandos
def comandos(update: Update, context):
    message = "Os comandos disponíveis são:\n\n/tutorial\n/assinar\n/suporte\n/ajuda"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Função para lidar com mensagens que não correspondam a comandos
def unknown_command(update: Update, context):
    message = "Desculpe, não entendi sua mensagem. Digite /start para começarmos a conversa, /tutorial para aprender como acessar o Grupo VIP exclusivo para membros, a partir do nível Inspetor ou /comandos e verifique as opções disponíveis para nossa conversa."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Função para verificar a assinatura do usuário
def verificar_assinatura(update: Update, context):
    user_id = update.message.text.strip()
    if is_youtube_member('x', user_id):
        message = "Verificação concluída com sucesso. Você é um membro do canal!"
    else:
        message = "Não encontramos sua assinatura. Por favor, certifique-se de que forneceu o ID correto e que é membro a partir do nível Inspetor."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    # Configuração do bot e dos comandos
    bot_token = "x"
    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("tutorial", tutorial))
    dispatcher.add_handler(CommandHandler("assinar", assinar))
    dispatcher.add_handler(CommandHandler("suporte", suporte))
    dispatcher.add_handler(CommandHandler("ajuda", ajuda))
    dispatcher.add_handler(CommandHandler("comandos", comandos))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), verificar_assinatura))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), unknown_command))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()





















