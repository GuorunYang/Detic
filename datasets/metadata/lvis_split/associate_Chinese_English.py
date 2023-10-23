import os


def load_word_dict(word_pth):
    dict_c2e = {}
    dict_e2c = {}
    with open(word_pth, "r") as f:
        word_lines = f.readlines()
        for ln in word_lines:
            ln = ln.strip()
            words = ln.split()
            chinese_word = words[-1]
            english_word = words[1][:-1]
            if chinese_word not in dict_c2e:
                dict_c2e[chinese_word] = [english_word]
            else:
                dict_c2e[chinese_word].append(english_word)
                # print("Chinese word {} is in the dict: {} vs {}".format(
                #     chinese_word, dict_c2e[chinese_word], english_word 
                # ))
            if english_word not in dict_e2c:
                dict_e2c[english_word] = chinese_word
            else:
                dict_e2c[english_word].append(chinese_word)

                # print("English word {} is in the dict: {} vs {}".format(
                #     english_word, dict_e2c[english_word], chinese_word 
                # ))
    return dict_c2e, dict_e2c

if __name__ == "__main__":
    base_dir = "/home/guorun.yang/Public/Detic/datasets/metadata/lvis_split"
    word_pth = os.path.join(base_dir, "L1/lvis_word_select_by_chatGPT_English-Chinese.txt")
    dict_c2e, _ = load_word_dict(word_pth)
    l2_dir = os.path.join(base_dir, "L2")
    l2_list = os.listdir(l2_dir)
    for list_fn in l2_list:
        ch_list_pth = os.path.join(l2_dir, list_fn)
        en_list_pth = os.path.join(l2_dir, list_fn.replace('Chinese', 'English'))
        ch_lines = []
        en_lines = []
        with open(ch_list_pth, 'r') as f:
            ch_lines = f.readlines()
            for ch_word in ch_lines:
                en_word_list = dict_c2e[ch_word.strip()]
                for en_word in en_word_list:
                    en_lines.append(en_word + '\n')
        with open(en_list_pth, 'w') as f:
            f.writelines(en_lines)
