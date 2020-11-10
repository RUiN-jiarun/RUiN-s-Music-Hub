var playlist = {
    musiclist : [],
    imglist : [],
    namelist : [],
    artistlist : []
}

var title = document.getElementById("songName");
var artist = document.getElementById("artist");
var index = document.getElementById("hidden_tag").innerText;
var img = document.getElementById("album");
// var needle = document.getElementById("needle");
// var diskCover = [$('.disk-cover:eq(0)'), $('.disk-cover:eq(1)'), $('.disk-cover:eq(2)')];
var music = document.getElementById("player");
var list = document.getElementById("lst");
var info = document.getElementsByClassName("in");

function getMusic()
{
    $(".bg").css('background-image', 'url(../../static' + playlist.imglist[index] + ')');
    music.src = '../../static' + playlist.musiclist[index];
    img.src = '../../static' + playlist.imglist[index];
    title.innerHTML = playlist.namelist[index];
    artist.innerHTML = playlist.artistlist[index];
}

function writeList()
{
    var i;
    for (i = 0; i < info.length; i++)
    {
        info[i].innerHTML = playlist.namelist[i];
    }
}

// 碟片动画
changeAnimationState = function ($ele, state)
{
    $ele.css({
        'animation-play-state': state,
        '-webkit-animation-play-state': state
    });
};

// 动画控制
function anicontrol()
{
    if (music.paused)
    {
        //changeAnimationState(diskCover[0], 'paused');
        changeAnimationState($('.disk-cover:eq(0)'), 'paused');
        //changeAnimationState(diskCover[2], 'paused');
        $('#needle').removeClass("resume-needle").addClass("pause-needle");
    }
    else
    {
        //changeAnimationState(diskCover[0], 'running');
        changeAnimationState($('.disk-cover:eq(0)'), 'running');
        //changeAnimationState(diskCover[2], 'running');
        $('#needle').removeClass("pause-needle").addClass("resume-needle");
    }
}

function next()
{
    if (index < playlist.namelist.length)
    {
        index++;
        getMusic();
        writeList();
        music.play();
    }
}

function prev()
{
    if(index > 0)
    {
        index--;
        getMusic();
        writeList();
        music.play();
    }
}

function showList()
{
    list.style.width = "250px";
    $('#l').removeAttr("onclick").attr("onclick", "hideList()");
}

function hideList()
{
    list.style.width = "0";
    $('#l').removeAttr("onclick").attr("onclick", "showList()");
}


$(document).ready(function()
{
    var url = '../../static/js/Hip-hop_playlist.json';
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            playlist.musiclist = data.music;
            playlist.imglist = data.cover;
            playlist.namelist = data.title;
            playlist.artistlist = data.artist;
        },
        error : function() {
            alert('load json error');
        }
    });

    setTimeout("writeList(); getMusic(); music.play();", 200);
    setInterval("anicontrol();", 50);
})
