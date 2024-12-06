def serve_client_lobby(conn, addr, usrn, selection):
    send(conn, splash.waiting())
    while True:
        if lobby_status(selection):
            for i, func in Questions[selection].items():
                player_name = players[usrn]["Name"]
                try:
                    if player_name == usrn:
                        print(f"{player_name} : got question {i}")
                        log.logIt(f"{player_name} : got question {i}")
                except KeyError:
                    print(f"KeyError: 'Name' not found for user {usrn}")
                    send(conn, "An error occurred. Please try again.")
                send(conn, "!" + func())
                msg_len = conn.recv(64).decode('utf-8')
                if msg_len:
                    msg_len = int(msg_len)
                    message = conn.recv(msg_len).decode('utf-8')
                    try:
                        if player_name == usrn:
                            print(f"{player_name} Answered: {i} with {message[1:]}")
                            log.logIt(f"{player_name} Answered: {i} with {message[1:]}")
                    except KeyError as e:
                        log.logIt(f"KeyError: {e}")
                        send(conn, "An error occurred. Please try again. Happened with the Lobby accessing a Name")
                        break
                    if message == "DISCON":
                        update_conns()
                        remove_player(usrn)
                        break
                    if message[1:] == Answers[selection][i]:
                        players[usrn].update({"GP": players[usrn]["GP"] + 1})
                        print(f"{player_name} Got It Correct!")
                        log.logIt(f"{player_name} Got It Correct!")
                        send(conn, splash.correct())
                    elif message[1:] in ['A', 'B', 'C']:
                        print(f"{player_name} Got It Wrong! Womp Womp")
                        log.logIt(f"{player_name} Got It Wrong! Womp Womp")
                        send(conn, splash.wrong())
                    else:
                        incorrecInput = False
                        while incorrecInput:
                            send(conn, "Incorrect Input Type")
                            send(conn, "!"+func())
                            msg_len = conn.recv(64).decode('utf-8')
                            if msg_len:
                                msg_len = int(msg_len)
                                message = conn.recv(msg_len).decode('utf-8')
                                try:
                                    if player_name == usrn:
                                        print(f"{player_name} Answered: {i} with {message[1:]}")
                                        log.logIt(f"{player_name} Answered: {i} with {message[1:]}")
                                except KeyError as e:
                                    log.logIt(f"KeyError: {e}")
                                    send(conn, "An error occurred. Please try again. Happened with the Lobby accessing a Name")
                                    break
                                if message == "DISCON":
                                    update_conns()
                                    remove_player(usrn)
                                    break
                                if message[1:] == Answers[selection][i]:
                                    players[usrn].update({"GP": players[usrn]["GP"] + 1})
                                    print(f"{player_name} Got It Correct!")
                                    log.logIt(f"{player_name} Got It Correct!")
                                    send(conn, splash.correct())
                                    break
                                elif message[1:] in ['A', 'B', 'C']:
                                    print(f"{player_name} Got It Wrong! Womp Womp")
                                    log.logIt(f"{player_name} Got It Wrong! Womp Womp")
                                    send(conn, splash.wrong())
                                    break
            send(conn, splash.scoreBoard(players))
            if int(i) > 6:
                break
    send(conn, splash.winCondition(lobby[selection]))
    #TODO Play again?
    return True