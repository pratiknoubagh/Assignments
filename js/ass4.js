function toTitleCase(sentence) {
    
    const words = sentence.split(' ');
  
    
    const titleCaseWords = words.map(word => {
      
      const firstChar = word[0].toUpperCase();
      const restOfString = word.slice(1).toLowerCase();
      return firstChar + restOfString;
    });
  
    
    const titleCaseSentence = titleCaseWords.join(' ');
  
    return titleCaseSentence;
  }
  
  // Example usage:
  const inputSentence = "this is a sample sentence";
  const titleCaseResult = toTitleCase(inputSentence);
  console.log(titleCaseResult); // Output: "This Is A Sample Sentence"
  