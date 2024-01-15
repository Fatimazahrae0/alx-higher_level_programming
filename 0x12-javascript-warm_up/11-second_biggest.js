#!/usr/bin/node

// Function to find the second biggest integer
function secondBiggest(arr) {
  if (arr.length <= 2) {
    return 0;
  }

  let first = parseInt(arr[2]);
  let second = parseInt(arr[3]);

  for (let i = 2; i < arr.length; i++) {
    let num = parseInt(arr[i]);

    if (num > first) {
      second = first;
      first = num;
    } else if (num > second && num < first) {
      second = num;
    }
  }

  return second;
}

// Parse command line arguments
const args = process.argv.slice(2);

// Call the function and print the result
console.log(secondBiggest(args));
