function main(){
	var currentDate = new Date();
	document.getElementById("clock").innerHTML = currentDate.getHours() + ':' + currentDate.getMinutes();
}