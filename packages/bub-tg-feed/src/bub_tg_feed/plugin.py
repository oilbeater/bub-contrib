from bub import hookimpl
from bub.channels import Channel
from bub.types import MessageHandler


@hookimpl
def provide_channels(message_handler: MessageHandler) -> list[Channel]:
    from .amqp_channel import AMQPChannel

    return [AMQPChannel(message_handler)]
