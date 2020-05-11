#!/usr/bin/node

const dict = require('./101-data').dict;

const allValues = Object.values(dict);
const allKeys = Object.keys(dict);
const newDict = {};
allValues.map(value => {
  newDict[value] = allKeys.filter(key => dict[key] === value);
});
console.log(newDict);
