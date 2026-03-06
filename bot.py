import telegram
from time import sleep
from ton_monitor import fetch_new_deployment_data
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

# Initialize Telegram Bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def send_deployment_alert(deployment):
    """
    Sends a new deployment notification to Telegram channel.
    """
    message = (
        f"🚀 New Token Deployed!\n\n"
        f"**Contract Address**: {deployment['address']}\n"
        f"**Deployer**: {deployment['deployer']}\n"
        f"**Initial Value**: {deployment['value']} TON\n\n"
        f"Stay tuned for more updates! 🌐"
    )

    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode="Markdown")

def main():
    print("👾 TON Deployment Bot is live...")

    while True:
        sleep(10)  # Poll every 10 seconds
        new_tokens = fetch_new_deployment_data()
        
        for token in new_tokens:
            send_deployment_alert(token)

if __name__ == "__main__":
    main()
