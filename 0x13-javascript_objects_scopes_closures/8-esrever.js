#!/usr/bin/node

exports.esrever = function (list) {
	const reverse = [];
	for (item of list) {
		reverse.unshift(item);
	}
	return reverse;
}
