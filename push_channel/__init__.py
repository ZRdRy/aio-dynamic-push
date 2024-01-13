from ._push_channel import PushChannel
from .bark import Bark
from .dingtalk_bot import DingtalkBot
from .feishu_bot import FeishuBot
from .server_chan_turbo import ServerChanTurbo
from .wecom_apps import WeComApps

push_channel_dict = {}


def get_push_channel(config):
    channel_type = config.get("type", None)
    if channel_type == "serverChan_turbo":
        return ServerChanTurbo(config)
    if channel_type == "wecom_apps":
        return WeComApps(config)
    if channel_type == "dingtalk_bot":
        return DingtalkBot(config)
    if channel_type == "feishu_bot":
        return FeishuBot(config)
    if channel_type == "bark":
        return Bark(config)
    else:
        raise ValueError(f"不支持的通道类型: {channel_type}")