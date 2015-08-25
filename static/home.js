function main(){
	var currentDate = new Date();
	var minutes = currentDate.getMinutes();
	if (minutes < 10)
		minutes = '0' + String(minutes)
	var hours = currentDate.getHours();
	if (hours < 10)
		hours = '0' + String(hours)
	document.getElementById("clock").innerHTML = hours + ':' + minutes;
}