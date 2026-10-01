from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from app.config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN
from app.agent.sherlock import Sherlock


app = App(
    token=SLACK_BOT_TOKEN
)

sherlock = Sherlock()


@app.event("app_mention")
def handle_mention(event, say):

    message = event.get("text", "")

    response = sherlock.respond(message)

    say(response)


def start():

    handler = SocketModeHandler(
        app,
        SLACK_APP_TOKEN
    )

    handler.start()