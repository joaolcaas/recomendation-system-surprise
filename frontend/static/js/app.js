const serviceUrl='http://localhost:8080/'

const changeUrl = function () {
    uidValue = document.getElementById('uid').value
    num_id = `${serviceUrl}uid/?url=${encodeURIComponent(uidValue)}`
    const httpRequest = new XMLHttpRequest();
    httpRequest.open("GET", num_id, false);
  	httpRequest.send();
	responseRequest = JSON.parse(httpRequest.responseText)
    var element = document.getElementById('uidList')
    element.innerHTML = responseRequest
    
}