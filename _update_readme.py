import re, subprocess

OLD_SHA = "7463fefd0f55ae2ba0b919e06527588022893495"

DELETE_KEYS = [
    "luffy/deepscaler/utils.py:45",
    "luffy/deepscaler/utils.py:46",
    "luffy/deepscaler/utils.py:47",
    "luffy/deepscaler/utils.py:48",
    "luffy/deepscaler/utils.py:49",
    "luffy/verl/verl/protocol.py:114",
    "luffy/verl/verl/protocol.py:115",
    "luffy/verr/PLACEHOLDER",
]

RENUMBER = {
    "luffy/deepscaler/utils.py:50": 45,
    "luffy/verr/PLACEHOLDER": 0,
}
