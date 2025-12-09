from shahadbot import get_cohere_response, synthesize_and_play_speech

def main():
    print("ShahadBot CLI is running. Type 'exit' to exit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye")
            break

        #user_message = "Answer briefly: " + user_message
        reply_text = get_cohere_response(user_input)
        print(f"ShahadBot: {reply_text}")

        synthesize_and_play_speech(reply_text, filename="response.mp3", play_audio=True)

if __name__ == "__main__":
    main()
