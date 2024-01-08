#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) { // This function calls a function passed 'x' times
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
