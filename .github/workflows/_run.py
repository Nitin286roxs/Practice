"""
class for message decypt
"""

import sys
class MessageDecryptClass:

    """
    init method or constructor
    """

    def __init__(self):
        self.alphabates = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.emblem = {'LAND': 'PANDA', 'WATER': 'OCTOPUS',
                       'ICE': 'MAMMOTH', 'AIR': 'OWL', 'FIRE': 'DRAGON'}

    def decrypt_char(self, msg, key):
        """
        init method or constructor
        """
        decrypt_msg = ""
        for char in msg:
            decrypt_msg += self.alphabates[self.alphabates.index(char)-key]
        return decrypt_msg

    def decrypt_message(self, lines):
        """
        Method to Decode Message
        """
        supporter = []
        for line in lines:
            _msg = line.split(" ")
            emb = _msg[0]
            msg = "".join(_msg[1:])
            key = len(self.emblem[emb])
            decrypt_msg = self.decrypt_char(msg, key)
            is_supporter = True
            for char in self.emblem[emb]:
                if char not in decrypt_msg:
                    is_supporter = False
                    break
            if is_supporter:
                supporter.append(emb)
        if len(supporter) >= 3:
            print("SPACE "+" ".join(supporter))
        else:
            print("NONE")
if __name__ == "__main__":
    INPUT_FILE = sys.argv[1]  # input filepath
    LINES = [line.strip()for line in open(INPUT_FILE, "r").readlines()]

    DCRPT_OBJ = MessageDecryptClass()
    DCRPT_OBJ.decrypt_message(LINES)
