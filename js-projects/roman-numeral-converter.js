function convertToRoman(num) {
    const romanNumerals = {
        M: 1000,
        CM: 900,
        D: 500,
        CD: 400,
        C: 100,
        XC: 90,
        L: 50,
        XL: 40,
        X: 10,
        IX: 9,
        V: 5,
        IV: 4,
        I: 1
    };

    let answer = "";
    for (let prop in romanNumerals) {
        while (num >= romanNumerals[prop]) {
            answer += prop;
            num -= romanNumerals[prop];
        }
    }

    return answer;
   }
   
console.log(convertToRoman(36));
console.log(convertToRoman(140));
console.log(convertToRoman(457));