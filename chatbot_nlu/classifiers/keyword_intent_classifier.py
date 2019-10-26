'''
@Author  :   Xu

@Software:   PyCharm

@File    :   keyword_intent_classifier.py.py

@Time    :   2019-09-25 14:23

@Desc    :

'''

from typing import Any, Optional, Text
import json
import pathlib
import os

from chatbot_nlu.components import Component
from chatbot_nlu.training_data import Message


basedir = str(pathlib.Path(os.path.abspath(__file__)).parent.parent)

intent_dict = {
 	"JS": "接受",
 	"SD": "收到",
 	"QG": "钱够",
 	"ZHD": "账号对",
 	"BZD": "不知道",
 	"MSD": "没收到",
 	"YH_WZCG": "已还-未知成功（打了）",
 	"CL_MK": "存了-没扣",
 	"CL_DK": "存了-待扣",
 	"HWL+NHL": "还完了|弄好了",
 	"XSCG": "显示成功",
 	"JT": "今天",
 	"FJTYH": "非今天已还",
 	"HMH": "还没还",
 	"MQH": "没钱还",
 	"TR": "通融",
 	"JTHH": "今天会还",
 	"KXRQ": "可信日期",
 	"MYWT": "没有问题",
 	"SM_APP": "什么APP",
 	"YTC": "要退车",
 	"BGL": "不管了",
 	"YJTC": "已经退车",
 	"ZJY": "自己用",
 	"TDDM": "听得到吗",
 	"HCDS": "还差多少",
 	"ZNJ_DS": " 滞纳金多少",
 	"ZNJ_WHY": "为什么会产生滞纳金",
 	"KKSJ": "扣款时间",
 	"KXEL": "卡限额了",
 	"ZMH+CNL": "怎么还+存哪里",
 	"BHN": "不会弄",
 	"ZJZMCZ": "自己还怎么操作",
 	"XXHK": "线下还款",
 	"KHMC": "开户名称",
 	"KHH": "开户行",
 	"ZH": "帐户",
 	"KFDH": "客服电话",
 	"SB": "生病",
 	"PC": "破产",
 	"ZSL+MXH": "在山里+没信号",
 	"XXWT": "详细问题",
 	"ZM": "在忙",
 	"NLD": "哪里的",
 	"JQR_WT": "机器人话题",
 	"MKH": "没空还",
 	"ZYD": "在异地",
 	"ZT": "暂停",
 	"TJH": "套近乎",
 	"LJDH": "另记电话",
 	"JZBZ": "机主不在",
 	"FMB": "非目标",
 	"SRZP": "骚扰诈骗",
 	"HZHM": "杭州号码",
 	"BRH+BRY": "别人还+别人用",
 	"BRY": "别人用",
 	"NQYZ": "哪期月租",
 	"HYHK": "换银行卡",
 	"YSZX": "影响征信",
 	"BYSB": "不要上报",
 	"BX_DP_YZ": "想用保险理赔抵用月租",
 	"CLYWT": "车辆有问题",
 	"MC_WHY_ZC": "买车怎么是租车",
 	"TBZJ": "退保证金"
 }
intend_reverse = {j: i for i, j in intent_dict.items()}
key_word = json.load(open(basedir + '/resource/intends2.json', 'r'))
maps = sorted(key_word.keys(), key=lambda x: len(key_word[x]))

def build_stand_sen(text):
	if text == "######":
		return "start"
	for i in maps:
		for j in key_word[i]:

			if j in text:
				print(i)
				return intend_reverse[i]
	return "other"

class KeywordIntentClassifier(Component):

	name = "intent_classifier_keyword"

	provides = ["intent"]

	his = ["hello", "hi", "hey"]


	def process(self, message, **kwargs):
		# type: (Message, **Any) -> None

		intent = {"name": self.parse(message.text), "confidence": 1.0}
		message.set("intent", intent, add_to_output=True)

	def parse(self, text):
		# type: (Text) -> Text

		_text = text.lower()

		return build_stand_sen(_text)
