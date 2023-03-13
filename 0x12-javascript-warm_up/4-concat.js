#!/usr/bin/node

'use strict';

const args = process.argv.slice(2);

const arg1 = args[0] || 'undefined';
const arg2 = args[1] || 'undefined';

console.log(`${arg1} is ${arg2}`);
