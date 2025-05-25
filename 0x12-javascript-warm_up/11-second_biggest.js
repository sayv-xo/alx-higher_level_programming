#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let max;
  let max2;

  if (Number(process.argv[2]) < Number(process.argv[3])) {
    max2 = Number(process.argv[2]);
    max = Number(process.argv[3]);
  } else {
    max = Number(process.argv[2]);
    max2 = Number(process.argv[3]);
  }

  const n = process.argv.length;

  for (let i = 4; i < n; i++) {
    const num = Number(process.argv[i]);
    if (num > max2 && num < max) {
      max2 = num;
    } else if (num > max) {
      max2 = max;
      max = num;
    }
  }
  console.log(max2);
}
