#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	let occ = 0;
	for (item of list) {
		if ( searchElement == item) {
			occ += 1;
		}
	}
	return occ;
}
