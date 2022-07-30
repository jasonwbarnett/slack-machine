import logging
from machine_v2.plugins.base import MachineBasePlugin, Message
from machine_v2.plugins.decorators import listen_to, respond_to

logger = logging.getLogger(__name__)


class PingPongPlugin(MachineBasePlugin):
    """Playing Ping Pong"""

    @listen_to(r'^ping$')
    async def listen_to_ping(self, msg: Message):
        """ping: serving the ball"""
        logger.debug("Ping received with msg: %s", msg)
        await msg.say("pong")

    @listen_to(r'^pong$')
    async def listen_to_pong(self, msg: Message):
        """pong: returning the ball"""
        logger.debug("Pong received with msg: %s", msg)
        await msg.say("ping")


class HelloPlugin(MachineBasePlugin):
    """Greetings"""

    @respond_to(r'^(?P<greeting>hi|hello)')
    async def greet(self, msg: Message, greeting):
        """hi/hello: say hello to the little guy"""
        logger.debug("Greeting '%s' received", greeting)
        await msg.say(f"{greeting.title}, {msg.at_sender}!")