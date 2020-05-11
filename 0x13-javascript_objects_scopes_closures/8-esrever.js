#!/usr/bin/node

exports.esrever = function (list) {
  let lsLen = list.length;
  const half = parseInt(lsLen / 2);

  for (let i = 0; i < half; i++) {
    [list[i], list[lsLen - 1]] = [list[lsLen - 1], list[i]];
    lsLen -= 1;
  }
  return list;
};
