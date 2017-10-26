let arr = [1, 2, 3, 4, 5, 6, 7, 8];

function originalFilter(array){
	
	if (array.length === 1){
		return array;
	}

	var filtered = [];
	for (var i = 0; i < array.length; i++){
		if (i % 2 !== 0){
			filtered.push(array[i]);
		}
	}

	if(filtered.length !== 1){
		return originalFilter(filtered.reverse());
	}
}

console.log(originalFilter(arr));