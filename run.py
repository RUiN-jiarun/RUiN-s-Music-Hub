from flask import *
from datetime import timedelta
import os
import json

app = Flask(__name__)
app.send_file_max_age_default = timedelta(seconds=1)

def rename_folder(file_dir):
    dirs = os.listdir(file_dir)
    for dir in dirs:
        s = dir.replace(' ','').replace('&','_')
        oldname = os.path.join(file_dir, dir)
        newname = os.path.join(file_dir, s)
        if dir != s:
            os.rename(oldname, newname)

def file_handle(file_dir, folder_name):
    imglst = []
    muslst = []
    txtlst = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':  # 想要保存的文件格式
                imglst.append(os.path.join('/3180105640/{}'.format(folder_name), file).replace('\\','/'))
            elif os.path.splitext(file)[1] == '.mp3':
                muslst.append(os.path.join('/3180105640/{}'.format(folder_name), file).replace('\\','/'))
            elif os.path.splitext(file)[1] == '.txt':
                with open(os.path.join(root, file), 'r') as f:
                    meta = eval(f.read())
                    l = ' - '.join([str(meta['Creator']).strip("[']").strip('\"'), str(meta['Title']).strip("[']")])
                    txtlst.append(l)
    return zip(muslst, imglst, txtlst)

def get_playlist_json(file_dir, folder_name):
    music = []
    img = []
    artist = []
    title = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':  # 想要保存的文件格式
                img.append(os.path.join('/3180105640/{}'.format(folder_name), file).replace('\\','/'))
            elif os.path.splitext(file)[1] == '.mp3':
                music.append(os.path.join('/3180105640/{}'.format(folder_name), file).replace('\\','/'))
            elif os.path.splitext(file)[1] == '.txt':
                with open(os.path.join(root, file), 'r') as f:
                    meta = eval(f.read())
                    title.append(meta['Title'])
                    artist.append(meta['Creator'])
    dict = {"artist":artist, "title":title, "music":music, "cover":img}
    filename = 'static/js/{}_playlist.json'.format(folder_name)
    with open(filename, 'w') as f:
       json.dump(dict, f)



zippedlst1 = file_handle(r"static/3180105640/Hip-hop", "Hip-hop")
zippedlst2 = file_handle(r"static/3180105640/Rock_Metal", "Rock_Metal")

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/hip_hop/')
def hip_hop():
    zippedlst1 = file_handle(r"static/3180105640/Hip-hop", "Hip-hop")
    return render_template('hip-hop.html', lst=zippedlst1)

@app.route('/rock_metal/')
def rock_metal():
    zippedlst2 = file_handle(r"static/3180105640/Rock_Metal", "Rock_Metal")
    return render_template('rock_metal.html', lst=zippedlst2)

@app.route('/convert_demo/')
def convert_demo():
    # return render_template('player_demo.html')
    return render_template('converter_demo.html')

@app.route('/player/hiphop/?&<id>')
def player_hiphop(id):
    zippedlst1 = file_handle(r"static/3180105640/Hip-hop", "Hip-hop")
    return render_template('player_hiphop.html', id=id, lst=zippedlst1)

@app.route('/player/rock/?&<id>')
def player_rock(id):
    zippedlst2 = file_handle(r"static/3180105640/Rock_Metal", "Rock_Metal")
    return render_template('player_rock.html', id=id, lst=zippedlst2)


if __name__ == '__main__':
    rename_folder(r"static/3180105640/")
    get_playlist_json(r"static/3180105640/Hip-hop", "Hip-hop")
    get_playlist_json(r"static/3180105640/Rock_Metal", "Rock_Metal")
    app.run(debug=True)