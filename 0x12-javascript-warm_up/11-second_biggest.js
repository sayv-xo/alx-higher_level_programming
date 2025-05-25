#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let max;
  let max_2;

  if (Number(process.argv[2]) < Number(process.argv[3])) {
    max_2 = Number(process.argv[2]);
    max = Number(process.argv[3]);
  } else {
    max = Number(process.argv[2]);
    max_2 = Number(process.argv[3]);
  }

  const n = process.argv.length

  for (i = 4; i < n; i++) {
    let num = Number(process.argv[i]);
    if (num > max_2 && num < max) {
      max_2 = num;
    } else if (num > max) {
      max_2 = max;
      max = num;
    }
  }
  console.log(max_2)
}
