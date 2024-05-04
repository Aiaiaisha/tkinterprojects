import socket
import random
from threading import Thread

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_add = "127.0.0.1"
port = 8000
server.bind((ip_add,port))
server.listen()

clients = []

questions = ["How do you say cat in japanese:\n a: nihongo\n b: neko\n c: nayami\n d: nai ",
             "How do you say sadness in japanese:\n a: kanashimi\n b: shiawase\n c: kurushimi\n d: okoru ",
             "How do you say disappear in japanese:\n a: mitoreteiru\n b: hibiiteru\n c: shinu\n d: kieru ",
             "How do you say rice in spanish:\n a: arroz\n b: pan\n c: paella\n d: fresa ",
             "How do you say cat in spanish:\n a: rata\n b: gato\n c: perro\n d: conejo ",]
answers = ["b","a","d","a","b"]

def clientthread(conn,addr):
    conn.send("Connected".encode("utf-8"))
    while True:
        try:
            message=conn.recv(2048).decode("utf-8")
            if message:
                print("<"+addr[0]+"> "+message)
                message_2_send = "<"+addr[0]+"> "+message
                #broadcast(message_2_send,conn)
            else:
                clients.remove(conn)
        except:
            continue
def get_rand_question():
    question_index = random.randint(0,len(questions)-1)
    question = questions[question_index]
    ans = answers[question_index]
    conn.send(question.encode("utf-8"))
    return question_index,question,ans

def remove_question(question_index):
    questions.remove(question_index)
    answers.remove(question_index)

while True:
    conn,addr = server.accept()
    clients.append(conn)
    score = 0
    print(addr[0]+" connected")

    new_thread = Thread(target=clientthread,args=(conn,addr))
    new_thread.start()

    question_index,question,ans= get_rand_question()
    remove_question(question_index)

    if conn.recv(2048).decode("utf-8") == ans:
        score +=1
        conn.send("Correct answer, +1 point").encode("utf-8")
    else:
        conn.send("Answer incorrect")
