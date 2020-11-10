'''
转换txt中的内容为json格式
直接运行一次即可，不需要运行第二次！！
包含的字段：Title标题，Creator创作者，Identifier标识符，Type类型，Format文件格式
'''
import os
import json

def rewrite_json(file_dir):

    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                with open(os.path.join(root, file), 'r') as f:
                    l = f.read().split(' - ')
                    Creator = []
                    Creator.append(l[0])
                    Title = []
                    Title.append(l[1])
                    Type = []
                    Type.append(os.path.basename(os.path.dirname(os.path.join(root, file))))
                    Identifier = []
                    Identifier.append(Type[0][0] + os.path.basename(os.path.join(root, file))[:-4])
                dict = {"Title":Title, "Creator":Creator, "Identifier":Identifier, "Type":Type, "Format":["mp3"]}
                # print(dict)
                with open(os.path.join(root, file), 'w') as nf:
                    json.dump(dict, nf)

def main():
    rewrite_json('static/3180105640/')

if __name__ == '__main__':
    main()