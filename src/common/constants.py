class MessageTypes:
    SEND_MESSAGE = "SendMessage"  # 新增消息类型常量
    ALERT = "Alert"
    USER_LOGIN = "UserLogin"
    SYSTEM_ERROR = "SystemError"


# 合并后的常量文件结构
class KafkaTopics:
    T_PYWEB_TEST = "t_pyweb_test"
