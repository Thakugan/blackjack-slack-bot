import os
import time
from slackclient import SlackClient
from dealer import Dealer
from admin import Admin

# possible commands, dealer will handle what to do with them
blackjack_actions = ['!show',
                     '!bet',
                     '!play',
                     '!hit',
                     '!double',
                     '!stay']


# admin user ids
admin_ids = [os.environ.get('ADMIN_ID')]

# instantiate the dealer
dealer = Dealer()
admin = Admin(dealer)

# instantiate Slack
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def handle_command(command, user, channel):
    # Admin commands that only I can send
    if command.split(' ', 1)[0] == "!admin":
        if user in admin_ids:
            admin.admin_do(command, user)
        else:
            response = "You do not have permission to execute this command"
            slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)

    # Blackjack commands
    elif command.split(' ', 1)[0] in blackjack_actions:
        dealer.do(command, user, channel)


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output:
                output['text'] = output['text'].lower()
                return output['text'], output['user'], output['channel']
    return None, None, None


def main():
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("BlackjackBot connected and running!")
        while True:
            command, user, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, user, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")


if __name__ == '__main__':
    main()