import tkinter
import os
import sys
def end():
    main.destroy()
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def caesar():
    message = message0.get().lower()
    print(message)
    encryptionValue = int(encriptyValue.get())
    newMessage = ""
    for i in range(len(message)):
        if not ord(message[i]) in [i for i in range(97, 123)]:
            newMessage += message[i]
        else:
            newChar = ord(message[i]) + encryptionValue
            if newChar > 122:
                newChar = newChar - 123 + 97
            newMessage += chr(newChar)
    encryptedMessageLabel["text"] = "encrypted message: " + newMessage
    print(newMessage)
def decrypt():
    message = message1.get().lower()
    print(message)
    decryptionValue = int(decValue.get())
    newMessage = ""
    for i in range(len(message)):
        if not ord(message[i]) in [i for i in range(97, 123)]:
            newMessage += message[i]
        else:
            newChar = ord(message[i]) - decryptionValue
            if newChar < 97:
                newChar = newChar + 26
            newMessage += chr(newChar)
    decryptedMessageLabel["text"] = "decrypted message: " + newMessage
    print(newMessage)
main = tkinter.Tk()
main.title("caesar algorithm")
messageLabel = tkinter.Label(main, text="message to encrypt:")
messageLabel.pack()
global message0
message0 = tkinter.Entry(main, width=50)
message0.pack()
encryptionValueLabel = tkinter.Label(main, text="encryption value:")
encryptionValueLabel.pack()
global encriptyValue
encriptyValue = tkinter.Entry(main, width=50)
encriptyValue.pack()
encryptButton = tkinter.Button(main, text="encrypt message", command=caesar)
encryptButton.pack()
encryptedMessageLabel = tkinter.Label(main, text="encrypted message:")
encryptedMessageLabel.pack()
spaceLabel = tkinter.Label(main, text=" ")
spaceLabel.pack()
messageLabel = tkinter.Label(main, text="message to decrypt:")
messageLabel.pack()
global message1
message1 = tkinter.Entry(main, width=50)
message1.pack()
decryptionValueLabel = tkinter.Label(main, text="decryption value:")
decryptionValueLabel.pack()
global decValue
decValue = tkinter.Entry(main, width=50)
decValue.pack()
decryptButton = tkinter.Button(main, text="decrypt message", command=decrypt)
decryptButton.pack()
decryptedMessageLabel = tkinter.Label(main, text="decrypted message:")
decryptedMessageLabel.pack()
restart = tkinter.Button(main, text="restart", command=restart_program)
restart.pack(side="left")
end = tkinter.Button(main, text="end", command=end)
end.pack(side="right")
main.mainloop()
