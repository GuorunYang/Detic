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
    word_dir = os.path.join(base_dir, "L3")
    word_list = os.listdir(word_dir)
    chinese_fn_list = []
    english_fn_list = []
    chinese_words = []
    english_words = []
    all_chinese_pth = os.path.join(base_dir, "L3/chinese_words_L3.txt")
    all_english_pth = os.path.join(base_dir, "L3/english_words_L3.txt")
    for fn in word_list:
        if fn.startswith("lvis_word_Chinese_") and fn.endswith(".txt"):
            chinese_fn_list.append(fn)
        elif fn.startswith("lvis_word_English_") and fn.endswith(".txt"):
            english_fn_list.append(fn)
    for chinese_fn in chinese_fn_list:
        chinese_word_pth = os.path.join(word_dir, chinese_fn)
        with open(chinese_word_pth, 'r') as f:
            word_lines = f.readlines()
            for ln in word_lines:
                # ln = ln.strip()
                if ln not in chinese_words:
                    chinese_words.append(ln)

    for english_fn in english_fn_list:
        english_word_pth = os.path.join(word_dir, english_fn)
        with open(english_word_pth, 'r') as f:
            word_lines = f.readlines()
            for ln in word_lines:
                # ln = ln.strip()
                if ln not in english_words:
                    english_words.append(ln)

    with open(all_chinese_pth, 'w') as f:
        f.writelines(chinese_words)

    with open(all_english_pth, 'w') as f:
        f.writelines(english_words)
