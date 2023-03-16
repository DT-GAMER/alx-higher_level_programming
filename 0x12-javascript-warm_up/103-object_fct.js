#!/usr/bin/node

const num = parseInt(process.argv[2]);

function incr (value) {
  return ++value;
}

if (isNaN(num)) {
  console.log('Missing number');
} else {
  console.log('Initial value:', num);
  const newNum = incr(num);
  console.log('New value:', newNum);
}
