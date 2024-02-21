from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mail_from = 'MAIL FROM: email.nyu.edu\r\n'
    clientSocket.send(mail_from.encode())
    recv2= clientSocket.recv(1024).decode()
    #print(recv2)
    
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpt_to = 'RCPT TO: email2.nyu.edu\r\n'
    clientSocket.send(rcpt_to.encode())
    recv3= clientSocket.recv(1024).decode()
    #print('RCPT TO Message: ',recv3)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data1 = 'DATA\r\n'
    clientSocket.send(data1.encode())
    recv4= clientSocket.recv(1024).decode()
    #print('DATA Message: ',recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode() + endmsg.encode())
    recv5= clientSocket.recv(1024).decode()
    #print('MSG Message: ',recv5)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    #clientSocket.send(endmsg.encode())
    #recv6= clientSocket.recv(1024).decode()
    #print('END MSG Message: ',recv6)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit_c = 'QUIT\r\n'
    clientSocket.send(quit_c.encode())
    recv7= clientSocket.recv(1024).decode()
    #print('QUIT Message: ',recv7)
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
