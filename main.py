all_ans = []


def target_id():
    a_cut = ["ID", "11", "12", "21", "22", "31", "32", "41", "42",
             "51", "52", "61", "62", "71", "72", "81", "82"]
    return a_cut


def mapping(tar, data):
    my_count = len(data)
    ans = []
    if my_count == 2:
        for cut in tar:
            if cut == "ID":
                ans.append(data[0])
            elif data[1] == cut:
                ans.append("X")
            else:
                ans.append("O")
        all_ans.append(ans)

    elif my_count == 3:
        for cut in tar:
            if cut == "ID":
                ans.append(data[0])
            elif data[1] == cut:
                ans.append("X")
            elif data[2] == cut:
                ans.append("X")
            else:
                ans.append("O")
        all_ans.append(ans)

    elif my_count == 4:
        for cut in tar:
            if cut == "ID":
                ans.append(data[0])
            elif data[1] == cut:
                ans.append("X")
            elif data[2] == cut:
                ans.append("X")
            elif data[3] == cut:
                ans.append("X")
            else:
                ans.append("O")
        all_ans.append(ans)

    elif my_count == 5:
        for cut in tar:
            if cut == "ID":
                ans.append(data[0])
            elif data[1] == cut:
                ans.append("X")
            elif data[2] == cut:
                ans.append("X")
            elif data[3] == cut:
                ans.append("X")
            elif data[4] == cut:
                ans.append("X")
            else:
                ans.append("O")
        all_ans.append(ans)


def to_file(file_name, tars, all_ans):
    with open(file_name, "w", encoding="utf-8") as f:
        for tar in tars:
            if tar == "82":
                f.write(f"{tar}\n")
            else:
                f.write(f"{tar},")
        for ans in all_ans:
            f.write("%s\n" % ans)


if __name__ == "__main__":
    tars = target_id()
    id1 = ["AAAAA", "11", "12"]
    id2 = ["BBBBB", "52", "71", "82"]
    id3 = ["CCCCC", "11", "21", "42"]
    id4 = ["DDDDD", "31", "22", "61"]
    id5 = ["EEEEE", "32", "41", "52", "82"]
    all_id = [id1, id2, id3, id4, id5]

    for id in all_id:
        mapping(tars, id)
    to_file("cut_id.txt", tars, all_ans)
