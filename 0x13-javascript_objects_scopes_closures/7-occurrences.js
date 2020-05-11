#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const res = list.filter(list => list === searchElement);
  return res.length;
};
