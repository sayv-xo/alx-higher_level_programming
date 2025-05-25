#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let max;
  let secondMax;

  if (Number(process.argv[2]) < Number(process.argv[3])) {
    secondMax = Number(process.argv[2]);
    max = Number(process.argv[3]);
  } else {
    max = Number(process.argv[2]);
    secondMax = Number(process.argv[3]);
  }

  const n = process.argv.length;

  for (let i = 4; i < n; i++) {
    const num = Number(process.argv[i]);
    if (num > secondMax && num < max) {
      secondMax = num;
    } else if (num > max) {
      secondMax = max;
      max = num;
    }
  }
  console.log(secondMax);
}
