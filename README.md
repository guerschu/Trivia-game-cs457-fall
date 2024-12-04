# Trivia Game 

We wanted to make a fun terminal co-op game where you and your friends can test your Trivia knowledge!

**Describe All Functions In Client**
1. Network Connection:
 * The code establishes a socket connection to the specified host and port.It sends and receives messages using a custom protocol, including a 64-byte header for message length.
2. Game Interaction:
* The start function initiates the game, sends the username to the server, and enters a loop to receive and process server messages. It handles different message types:
        Server messages: Printed to the console.
        Prompt messages (starting with "!"): Trigger user input and send the response to the server.


**Describe All Functions In Server**
1. Data Structures:
   * players: Stores information about connected players, including their IP address, game progress (GP), and selected category (SEL).
   * Answers: Contains correct answers for different categories.
   * Questions: Maps categories to their respective questions.

2. Server Functionality:
   * Connection Handling: Accepts incoming connections and spawns threads to handle each client.
    * Message Handling: Receives messages from clients, logs them, and sends responses.
    * Player Management: Updates the player's dictionary with player information and handles disconnections.

**Limitation of The Game**
* the lack of security is a main limitation of the game, if we were able to have more time to add the encryption would be a great way to get rid of this limitation
* There is no team-based part of the game that someone might want from this like they added into Kahoot.
* 

**How to play:**
1. **Start the server:** Run the `server.py` script. 'IP' 'Port number'
2. **Connect clients:** Run the `client.py` client is going to take three inputs from the terminal 'host IP address' 'port number' 'trivia' 'what kind of trivia you would like to play' 'the player name for the game'
3. **Pick Trivia:** We only have 'animal' trivia as an option, more soon to come to pick to be able to have a variety of fun trivia options
   * Animal
   * History
   * Locations
4. **Play the game:** Trying to get the most points by getting the most correct answers.  (not fully implemented yet)


**Technologies used:**
* Python 
* Sockets
* Splash
* Threading

**Text-Editor**
* We have decided to go with Visual Studio Code to work with when developing this game in Python

**Libraries**
*Here is where we will put what Libraries we are using as we find them*
*  sys
* socket
* selectors
* types
* Sockets
* Splash
* Threading

**Additional resources:**
* coming soon!

**Challenges**
* When it comes to making this game, we have run into many different issues that have caused hiccups along the way.
* When we first started this game we followed the code in the homework which led us astray since it was things we were not fully getting we were using, so we last minute decided to switch everything up and go with our way of coding it so the server and the client talk. We wanted to make a trivia game that seems closer to Kahoot in the way people who answer faster are the ones who get more points for their answers on correctness and time. We also learned how to communicate better about the code and functions we are thinking of since we cannot read the other brain.
* This project has taught us much about how to do things in a group and more about threading/server communications. 
