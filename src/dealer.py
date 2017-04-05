import os
from slackclient import SlackClient

class Dealer(object):
    def __init__(self):
        # The dealer's hand
        self.hand = []
        self.players = []
        self.table = []
        self.in_progress = False
        self.slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

    # The calling the general game functions
    def do(self, command, user, channel):
        # Functions for the general commands
        def show(self, command, user, channel):
            if command.split(' ')[1] == "scoreboard":
                response = "Temp scoreboard response"



                self.slack_client.api_call("chat.postMessage", text=response,
                                            channel=channel, as_user=True)
            elif command.split(' ')[1] == "hand":
                response = "Temp hand response"
                self.slack_client.api_call("chat.postMessage", text=response,
                                            channel=user, as_user=True)
            else:
                response = "The valid commands for 'show' are scoreboard and hand"
                self.slack_client.api_call("chat.postMessage", text=response,
                                            channel=channel, as_user=True)

        # def bet(self, command, user, channel):
        #
        #
        # def play(self, command, user, channel):
        #
        #
        # def hit(self, command, user, channel):
        #
        #
        # def double(self, command, user, channel):
        #
        #
        # def stay(self, command, user, channel):

        # Calling the appropriate function
        actions = {"show": show
                #    "bet": bet,
                #    "play": play,
                #    "hit": hit,
                #    "double": double,
                #    "stay": stay
                  }

        actions[command.split(' ', 1)[0]](self, command, user, channel)


    # Game management functions
    # def end_turn(self):
    #
    #
    # def end_hand(self):
