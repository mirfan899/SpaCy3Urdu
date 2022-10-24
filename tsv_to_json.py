# Convert .tsv file to dataturks json format. 
import json
import logging


def tsv_to_json_format(input_path, output_path, unknown_label):
    try:
        f = open(input_path, 'r', encoding="utf8")  # input file
        fp = open(output_path, 'w', encoding="utf8")  # output file
        data_dict = {}
        annotations = []
        label_dict = {}
        s = ''
        start = 0
        for line in f:
            if line[0:len(line) - 1] != 'ہے\tO':
                word, entity = line.split('\t')
                s += word + " "
                entity = entity[:len(entity) - 1]
                if entity != unknown_label:
                    if len(entity) != 1:
                        d = {'text': word, 'start': start, 'end': start + len(word)}
                        try:
                            label_dict[entity].append(d)
                        except:
                            label_dict[entity] = []
                            label_dict[entity].append(d)
                start += len(word) + 1
            else:
                data_dict['content'] = s.strip()
                s = ''
                label_list = []
                for ents in list(label_dict.keys()):
                    for i in range(len(label_dict[ents])):
                        if label_dict[ents][i]['text'] != '':
                            l = [ents, label_dict[ents][i]]
                            for j in range(i + 1, len(label_dict[ents])):
                                if label_dict[ents][i]['text'] == label_dict[ents][j]['text']:
                                    di = {'start': label_dict[ents][j]['start'], 'end': label_dict[ents][j]['end'] + 1,
                                          'text': label_dict[ents][i]['text']}
                                    l.append(di)
                                    label_dict[ents][j]['text'] = ''
                            label_list.append(l)

                for entities in label_list:
                    label = {'label': [entities[0]], 'points': entities[1:]}
                    annotations.append(label)
                data_dict['annotation'] = annotations
                annotations = []
                if data_dict["content"] and data_dict["annotation"]:
                    json.dump(data_dict, fp, ensure_ascii=False)
                    fp.write('\n')
                data_dict = {}
                start = 0
                label_dict = {}
    except Exception as e:
        logging.exception("Unable to process file" + "\n" + "error = " + str(e))
        return None


tsv_to_json_format("ner/100000.txt", 'ner/urdu_ner_dataset.json', 'abc')
