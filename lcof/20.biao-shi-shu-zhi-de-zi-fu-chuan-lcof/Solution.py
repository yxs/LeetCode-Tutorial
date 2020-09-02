from enum import Enum


class Solution:
    def isNumber(self, s: str) -> bool:
        State = Enum(
            "State",
            [
                "STATE_INITIAL",  # 头部 blank
                "STATE_INT_SIGN",  # 符号
                "STATE_INTEGER",  # 整数
                "STATE_POINT",  # 小数点，左侧有整数
                "STATE_POINT_WITHOUT_INT",  # 小数点，左侧无整数
                "STATE_FRACTION",  # 小数
                "STATE_EXP",  # e
                "STATE_EXP_SIGN",  # 指数 e 后的符号位
                "STATE_EXP_NUMBER",  # 指数 e 后的数字位
                "STATE_END",  # 尾部 blank
            ],
        )
        Chartype = Enum(
            "Chartype",
            [
                "CHAR_NUMBER",
                "CHAR_EXP",
                "CHAR_POINT",
                "CHAR_SIGN",
                "CHAR_SPACE",
                "CHAR_ILLEGAL",
            ],
        )

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch.lower() == "e":
                return Chartype.CHAR_EXP
            elif ch == ".":
                return Chartype.CHAR_POINT
            elif ch == "+" or ch == "-":
                return Chartype.CHAR_SIGN
            elif ch == " ":
                return Chartype.CHAR_SPACE
            else:
                return Chartype.CHAR_ILLEGAL

        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_SPACE: State.STATE_INITIAL,
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                Chartype.CHAR_SIGN: State.STATE_INT_SIGN,
            },
            State.STATE_INT_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
            },
            State.STATE_INTEGER: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_POINT: State.STATE_POINT,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_POINT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_POINT_WITHOUT_INT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
            },
            State.STATE_FRACTION: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_EXP: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SIGN: State.STATE_EXP_SIGN,
            },
            State.STATE_EXP_SIGN: {Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,},
            State.STATE_EXP_NUMBER: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SPACE: State.STATE_END,
            },
            State.STATE_END: {Chartype.CHAR_SPACE: State.STATE_END,},
        }

        st = State.STATE_INITIAL
        for ch in s:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return False
            st = transfer[st][typ]
        return st in [
            State.STATE_INTEGER,
            State.STATE_POINT,
            State.STATE_FRACTION,
            State.STATE_EXP_NUMBER,
            State.STATE_END,
        ]

