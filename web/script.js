'use strict'


let log = console.log.bind(console),
  id = val => document.getElementById(val),
  ul = id('ul'),
  gUMbtn = id('gUMbtn'),
  cntrl = id('cntrl'),
  cntrlimg = id('cntrlimg'),
  stream,
  recorder,
  counter=1,
  chunks,
  media;

  
  console.log("HEY")

  let mv = id('cntrl'),
      mediaOptions = {
        audio: {
          tag: 'audio',
          type: 'audio/wav',
          ext: '.wav',
          gUM: {audio: true}
        }
      };
  media = mediaOptions.audio;
  navigator.mediaDevices.getUserMedia(media.gUM).then(_stream => {
    stream = _stream;
    id('btns').style.display = 'inherit';
    recorder = new MediaRecorder(stream);
    recorder.ondataavailable = e => {
      chunks.push(e.data);
      if(recorder.state == 'inactive')  makeFile();
    };
    log('got media successfully');
  }).catch(log);

cntrl.onclick = e => {
  if (cntrl.value == 'Start') {
    chunks=[];
    recorder.start();
    cntrl.value = 'Stop';
    cntrlimg.src = "img/Breezeicons-status-22-mic-off.svg"
  } else if (cntrl.value == 'Stop') {
    recorder.stop();
    cntrl.value = 'Start';
    cntrlimg.src = "img/Breezeicons-status-22-mic-on.svg"
  }
}


function makeFile(){
  let blob = new Blob(chunks, {type: media.type })
    , url = URL.createObjectURL(blob)
    , li = document.createElement('li')
    , mt = document.createElement(media.tag)
    , hf = document.createElement('a')
  ;
  uploadAudio(blob)
}

function uploadAudio(wavData){
  var reader = new FileReader();
  reader.onload = function(event){
    var fd = new FormData();
    var wavName = encodeURIComponent('voice.wav');
    console.log("wavname = " + wavName);
    fd.append('fname', wavName);
    fd.append('data', event.target.result);
    $.ajax({
      type: 'POST',
      url: 'upload.php',
      data: fd,
      processData: false,
      contentType: false
    }).done(function(data) {
      //console.log(data);
      log.innerHTML += "\n" + data;
    });
  };
  reader.readAsDataURL(wavData);
}

