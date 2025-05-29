import colorama
from colorama import Fore,Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN} Welcome to sentiments {Style.RESET_ALL} ")

user_name = input(f"{Fore.CYAN} Please enter your name {Style.RESET_ALL}")
if not user_name:
    user_name = "Mystery name"

conversation_history = []

print(f"\n {Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a Sentence and I will anaylaz your sentence with Textblob and show you the sentiment.")
print(f"Type{Fore.YELLOW}'reset' {Fore.CYAN}, {Fore.YELLOW} 'history' {Fore.CYAN}," f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit, {Style.RESET_ALL}")

while True:
    user_input = input(f"{Fore.GREEN}>>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED} Please enter some text or valid command.{Style.RESET_ALL}")
        continue
    
    if user_input.lower() == "exit" :
        print(f"\n{Fore.BLUE} Exit sentiment spy. farewell agent{user_name}! {Style.RESET_ALL}")

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}")
        continue
    
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW} No concersation history yet {Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Convertion history {Style.RESET_ALL}")
            for idx, (text,polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "negative":
                    color = Fore.RED
                    emoji = "🥲"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{idx}. {color}{emoji} {text}"
                      f"(polarity: {polarity:.2f}, {sentiment_type}) {Style.RESET_ALL}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity> 0.25:
        sentiment_type = "positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity <-0.25:
        sentiment_type = "negative"
        color = Fore.RED
        emoji = "🥲"
    else:
        sentiment_type = "neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append((user_input,polarity,sentiment_type))

    print(f"{color}{emoji}{sentiment_type} sentiment detected! "
          f"(polarity: {polarity: 2f} {Style.RESET_ALL})")
