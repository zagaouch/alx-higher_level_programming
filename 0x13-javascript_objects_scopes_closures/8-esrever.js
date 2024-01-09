#!/usr/bin/node

exports.esrever = function (list) {
    const newList = [];
    for (let i = list.length - 1; i >= 0; i--) {
      newList.push(list[i]); // push is a method of Array that adds an element to the end of an array/list
    }
    return newList;
  };
