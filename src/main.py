from functions.chat_gpt import callChatGPT
from functions.voice_vox import textToVoice, playWav

if __name__ == "__main__":
    print("ずんだもんと会話したい内容を入力するのだ")
    playWav("wav_dir/start.wav")
    while True:
        try:
            print("あなた：")
            text = input()
            reply_chat_gpt = callChatGPT(text)
            print("ずんだもん：")
            print(reply_chat_gpt)
            textToVoice(reply_chat_gpt)
        except:
            print("エラーなのだ。もう一度内容を入力してほしいのだ")
            playWav("wav_dir/error.wav")
