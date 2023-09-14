function reverseString(inputString) {
  
  let reversed = "";

  
  for (let i = inputString.length - 1; i >= 0; i--) {
     
    reversed += inputString[i];
  }

  
  return reversed;
}


const originalString = "Hello, World!";
const reversed = reverseString(originalString);
console.log(reversed); 

