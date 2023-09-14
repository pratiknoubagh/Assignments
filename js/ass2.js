function countVowels(inputString) {
   
    const lowerCaseString = inputString.toLowerCase();
    
    
    const vowels = ["a", "e", "i", "o", "u"];
    
   
    let vowelCount = 0;
    
    
    for (let i = 0; i < lowerCaseString.length; i++) {
      const currentChar = lowerCaseString[i];
      
      
      if (vowels.includes(currentChar)) {
        vowelCount++;
      }
    }
    
    // Return the vowel count
    return vowelCount;
  }
  
  // Example usage:
  const inputString = "My name is Pratik Noubagh";
  const numberOfVowels = countVowels(inputString);
  console.log(`Number of vowels: ${numberOfVowels}`); // Output: Number of vowels: 3
  