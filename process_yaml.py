import yaml

with open(r'cv.yaml') as file:
    documents = yaml.full_load(file)

if __name__ == '__main__':
    # for item, doc in documents.items():
    #     print(item, ":", doc)

    for skill in documents['skills']:
        for k, v in skill.items():
            print(k, '->', end=' ')
            lst = v.split(',')
            for i in lst:
                print(i, end='')
            print('\n', end='')
