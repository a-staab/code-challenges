// Count from 1 to 20 in fizzbuzz fashion.

// Loop from 1 to 20 (inclusive). Each through, if the number
// is evenly divisible by 3, say 'fizz'. If the number is evenly
// divisible by 5, say 'buzz'. If the number is evenly divisible
// by both 3 and 5, say 'fizzbuzz'. Otherwise, say the number.


function fizzbuzz(start, stop) {
    for (var i = start; i <= stop; i++) {
        if (i % 15 === 0) {
            console.log('fizzbuzz');
        } else if (i % 3 === 0) {
            console.log('fizz');
        } else if (i % 5 === 0) {
            console.log('buzz');
        } else {
            console.log(i);
        }

    }
}

fizzbuzz(1, 20);
