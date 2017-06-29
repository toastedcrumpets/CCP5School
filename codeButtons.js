var pretags = document.getElementsByTagName("pre");

function saveTextAsFile()
{
    var text = this.parentElement.innerText;
    var textFileAsBlob = new Blob([text], {type:'text/plain'});
    var fileNameToSaveAs = "code.py";
    
    var downloadLink = document.createElement("a");
    downloadLink.download = fileNameToSaveAs;
    downloadLink.innerHTML = "Download File";
    if (window.webkitURL != null)
    {
        // Chrome allows the link to be clicked
        // without actually adding it to the DOM.
        downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
    }
    else
    {
        // Firefox requires the link to be added to the DOM
        // before it can be clicked.
        downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
        downloadLink.onclick = function(){
            document.body.removeChild(downloadLink);
        };
        downloadLink.style.display = "none";
        document.body.appendChild(downloadLink);
    }

    downloadLink.click();
}

for (var i = 0, max = pretags.length; i < max; ++i) {
    var iDiv = document.createElement('div');
    iDiv.className = 'codeDL';
    pretags[i].appendChild(iDiv);
    iDiv.addEventListener('click', saveTextAsFile);
    var button = document.getElementById('save');
}
