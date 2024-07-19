# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommendPhone(Action):

    def name(self) -> Text:
        return "action_recommend_phone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # 获取用户提到的手机型号
        phone_model = tracker.get_slot('phone_model')

        # 根据手机型号生成推荐（这里可以调用外部推荐系统或使用简单逻辑）
        recommendations = self.get_recommendations(phone_model)

        dispatcher.utter_message(text=f"根据您的需求，我推荐以下手机：{recommendations}")

        return []

    def get_recommendations(self, phone_model):
        # 这里可以实现推荐逻辑，例如调用推荐系统API
        if phone_model:
            return f"{phone_model}，以及相似的其他款式。"
        else:
            return "iPhone 14, Samsung Galaxy"

class ActionPhoneInfo(Action):

    def name(self) -> Text:
        return "action_phone_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # 获取用户提到的手机型号
        phone_model = tracker.get_slot('phone_model')

        # 获取手机介绍
        phone_info = self.get_phone_info(phone_model)

        dispatcher.utter_message(text=f"{phone_info}")

        return []

    def get_phone_info(self, phone_model):
        # 这里可以实现获取手机信息的逻辑
        phone_details = {
            "iPhone 14": "iPhone 14 是苹果公司于 2022 年推出的一款智能手机，采用铝合金边框和玻璃背板设计，提供优雅且坚固的手感，配备 6.1 英寸和 6.7 英寸的 Super Retina XDR 显示屏，带来沉浸式视觉体验。搭载 A15 仿生芯片，提供无与伦比的性能和能效，让您的操作更加流畅高效。摄像系统包括 1200 万像素的主摄像头和超广角摄像头，支持夜间模式和 4K Dolby Vision HDR 录制，捕捉每一个精彩瞬间。预装 iOS 16，带来全新的功能和更强大的隐私保护。支持 5G 网络和 MagSafe 无线充电，让您享受极速网络和便捷充电体验，并具备 IP68 级防水防尘功能，提供全方位保护。提供 128GB、256GB 和 512GB 的存储选项，满足不同用户的需求。无论是工作还是娱乐，iPhone 14 都是您的最佳选择。",
            "三星 Galaxy": "三星 Galaxy 系列涵盖从入门级到高端旗舰的多款智能手机，满足各类用户的需求。代表性的型号有 Galaxy S22 和 Galaxy Z Fold 4，无论您是追求顶尖科技还是独特设计，这两款都能超越您的期待。该系列采用先进的 AMOLED 显示屏，带来艳丽细腻的视觉效果，高刷新率让每一次滑动都畅快无比。搭载强大的 Exynos 或 Snapdragon 处理器，性能卓越，运行更快更顺畅。多摄像头系统支持夜间模式和 8K 视频录制，捕捉生活中的每一个精彩瞬间。运行基于 Android 的 One UI 界面，带来流畅直观的用户体验。支持 5G 网络，极速连接，快速充电和无线充电功能让您随时保持电力充沛，防水防尘设计和生物识别技术则提供全方位的保护和安全性。三星 Galaxy 系列让科技与时尚完美结合，满足您对性能、设计和创新的所有需求。"
        }
        return phone_details.get(phone_model, "抱歉，我没有关于该型号的信息。")
